import os
import re
from collections import defaultdict

LOCALES_PATH = "locales"
OUTPUT_FILE = "l10n_gen.py"

def kebab_to_snake(key):
    return key.replace("-", "_")

def extract_keys_from_ftl(ftl_path):
    with open(ftl_path, encoding="utf-8") as f:
        content = f.read()
    return re.findall(r"^([a-zA-Z0-9_-]+)\s*=", content, flags=re.MULTILINE)

def collect_keys_by_locale():
    locale_keys = defaultdict(set)

    for root, dirs, files in os.walk(LOCALES_PATH):
        for file in files:
            if file.endswith(".ftl"):
                locale = os.path.relpath(root, LOCALES_PATH)
                ftl_path = os.path.join(root, file)
                keys = extract_keys_from_ftl(ftl_path)
                locale_keys[locale].update(keys)

    return locale_keys

def generate_class(all_keys):
    all_method_names = set(kebab_to_snake(k) for keys in all_keys.values() for k in keys)

    lines = [
        "from fluent.runtime import FluentBundle, FluentResource",
        "import os\n",
        "class L10n:",
        "    def __init__(self, locale='ru-RU', path='locales'):",
        "        self.locale = locale",
        "        self.path = path",
        "        self.bundle = self._load_bundle()\n",
        "    def _load_bundle(self):",
        "        bundle = FluentBundle([self.locale])",
        "        folder = os.path.join(self.path, self.locale)",
        "        for file in os.listdir(folder):",
        "            if file.endswith('.ftl'):",
        "                ftl_path = os.path.join(folder, file)",
        "                with open(ftl_path, 'r', encoding='utf-8') as f:",
        "                    text = f.read()",
        "                    resource = FluentResource(text)",
        "                    bundle.add_resource(resource)",
        "        return bundle\n",
    ]

    for method_name in sorted(all_method_names):
        # Получаем оригинальный FTL-ключ
        ftl_key = method_name.replace("_", "-")
        lines += [
            f"    def {method_name}(self, **kwargs):",
            f"        msg = self.bundle.get_message('{ftl_key}')",
            "        if not msg or not msg.value:",
            f"            return f'[missing: {ftl_key}]'",
            "        return self.bundle.format_pattern(msg.value, kwargs)[0]\n"
        ]

    return "\n".join(lines)

def main():
    all_keys = collect_keys_by_locale()
    code = generate_class(all_keys)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"[✓] Сгенерирован файл: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
