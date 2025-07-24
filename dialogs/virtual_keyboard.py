from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button, Row, Group
from aiogram_dialog.widgets.text import Const
from asyncio import Lock


class VirtualKeyboard:
    def __init__(
        self,
        data_key: str = "typed_text",
        on_done: callable = None,
        on_update: callable = None,
    ):
        self.data_key = data_key
        self.on_done = on_done
        self.on_update = on_update

        self.lock = Lock()
        self.current_text = ""  # локальное состояние ввода
        self.current_lang = "en"  # состояние языка
        self.widget = self._build_keyboard()

    # Помощники для преобразования символа в id и обратно
    def char_to_id(self, ch: str) -> str:
        if ch.isascii() and ch.isalnum():
            return ch
        return f"ru_{ord(ch)}"

    def id_to_char(self, id_str: str) -> str:
        if id_str.startswith("ru_"):
            code = int(id_str[3:])
            return chr(code)
        return id_str

    async def on_char(self, c: CallbackQuery, button: Button, manager: DialogManager):
        async with self.lock:
            id_part = button.widget_id.split("_", 1)[1]
            char = self.id_to_char(id_part)
            self.current_text += char
            manager.dialog_data[self.data_key] = self.current_text
            if self.on_update:
                await self.on_update(manager)
            await manager.update({})

    async def on_backspace(self, c: CallbackQuery, button: Button, manager: DialogManager):
        async with self.lock:
            self.current_text = self.current_text[:-1]
            manager.dialog_data[self.data_key] = self.current_text
            if self.on_update:
                await self.on_update(manager)
            await manager.update({})

    async def on_done_click(self, c: CallbackQuery, button: Button, manager: DialogManager):
        async with self.lock:
            if self.on_done:
                await self.on_done(c, manager)
            else:
                await c.message.answer(f"Вы ввели: {self.current_text}")
                await manager.done()

    async def on_switch_lang(self, c: CallbackQuery, button: Button, manager: DialogManager):
        async with self.lock:
            self.current_lang = "ru" if self.current_lang == "en" else "en"
            self.widget = self._build_keyboard()
            await manager.update({})

    def _build_keyboard(self):
        layouts = {
            "en": ["1234567890", "qwertyuiop", "asdfghjkl", "zxcvbnm"],
            "ru": ["1234567890", "йцукенгшщзхъ", "фывапролджэ", "ячсмитьбю"],
        }

        rows = []
        for chars in layouts[self.current_lang]:
            row = [Button(Const(ch), id=f"vk_{self.char_to_id(ch)}", on_click=self.on_char) for ch in chars]
            rows.append(Row(*row))

        rows.append(Row(
            Button(Const("🌐 EN/РУ"), id="vk_switch_lang", on_click=self.on_switch_lang),
            Button(Const("⌫ Удалить"), id="vk_back", on_click=self.on_backspace),
            Button(Const("✅ Готово"), id="vk_done", on_click=self.on_done_click),
        ))

        return Group(*rows)
