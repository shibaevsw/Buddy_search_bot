from fluent.runtime import FluentBundle, FluentResource
import os

class L10n:
    def __init__(self, locale='ru-RU', path='locales'):
        self.locale = locale
        self.path = path
        self.bundle = self._load_bundle()

    def _load_bundle(self):
        bundle = FluentBundle([self.locale])
        folder = os.path.join(self.path, self.locale)
        for file in os.listdir(folder):
            if file.endswith('.ftl'):
                ftl_path = os.path.join(folder, file)
                with open(ftl_path, 'r', encoding='utf-8') as f:
                    text = f.read()
                    resource = FluentResource(text)
                    bundle.add_resource(resource)
        return bundle

    def back_btn(self, **kwargs):
        msg = self.bundle.get_message('back-btn')
        if not msg or not msg.value:
            return f'[missing: back-btn]'
        return self.bundle.format_pattern(msg.value, kwargs)[0]

    def cancel_btn(self, **kwargs):
        msg = self.bundle.get_message('cancel-btn')
        if not msg or not msg.value:
            return f'[missing: cancel-btn]'
        return self.bundle.format_pattern(msg.value, kwargs)[0]

    def confirm_btn(self, **kwargs):
        msg = self.bundle.get_message('confirm-btn')
        if not msg or not msg.value:
            return f'[missing: confirm-btn]'
        return self.bundle.format_pattern(msg.value, kwargs)[0]

    def create_meeting_btn(self, **kwargs):
        msg = self.bundle.get_message('create-meeting-btn')
        if not msg or not msg.value:
            return f'[missing: create-meeting-btn]'
        return self.bundle.format_pattern(msg.value, kwargs)[0]

    def create_meeting_header(self, **kwargs):
        msg = self.bundle.get_message('create-meeting-header')
        if not msg or not msg.value:
            return f'[missing: create-meeting-header]'
        return self.bundle.format_pattern(msg.value, kwargs)[0]

    def edit_btn(self, **kwargs):
        msg = self.bundle.get_message('edit-btn')
        if not msg or not msg.value:
            return f'[missing: edit-btn]'
        return self.bundle.format_pattern(msg.value, kwargs)[0]

    def edit_header(self, **kwargs):
        msg = self.bundle.get_message('edit-header')
        if not msg or not msg.value:
            return f'[missing: edit-header]'
        return self.bundle.format_pattern(msg.value, kwargs)[0]

    def find_meeteing_btn(self, **kwargs):
        msg = self.bundle.get_message('find-meeteing-btn')
        if not msg or not msg.value:
            return f'[missing: find-meeteing-btn]'
        return self.bundle.format_pattern(msg.value, kwargs)[0]

    def find_meeting_header(self, **kwargs):
        msg = self.bundle.get_message('find-meeting-header')
        if not msg or not msg.value:
            return f'[missing: find-meeting-header]'
        return self.bundle.format_pattern(msg.value, kwargs)[0]

    def hello(self, **kwargs):
        msg = self.bundle.get_message('hello')
        if not msg or not msg.value:
            return f'[missing: hello]'
        return self.bundle.format_pattern(msg.value, kwargs)[0]

    def main_menu_btn(self, **kwargs):
        msg = self.bundle.get_message('main-menu-btn')
        if not msg or not msg.value:
            return f'[missing: main-menu-btn]'
        return self.bundle.format_pattern(msg.value, kwargs)[0]

    def main_menu_header(self, **kwargs):
        msg = self.bundle.get_message('main-menu-header')
        if not msg or not msg.value:
            return f'[missing: main-menu-header]'
        return self.bundle.format_pattern(msg.value, kwargs)[0]

    def profile_btn(self, **kwargs):
        msg = self.bundle.get_message('profile-btn')
        if not msg or not msg.value:
            return f'[missing: profile-btn]'
        return self.bundle.format_pattern(msg.value, kwargs)[0]

    def profile_data(self, **kwargs):
        msg = self.bundle.get_message('profile-data')
        if not msg or not msg.value:
            return f'[missing: profile-data]'
        return self.bundle.format_pattern(msg.value, kwargs)[0]

    def profile_header(self, **kwargs):
        msg = self.bundle.get_message('profile-header')
        if not msg or not msg.value:
            return f'[missing: profile-header]'
        return self.bundle.format_pattern(msg.value, kwargs)[0]

    def settings_btn(self, **kwargs):
        msg = self.bundle.get_message('settings-btn')
        if not msg or not msg.value:
            return f'[missing: settings-btn]'
        return self.bundle.format_pattern(msg.value, kwargs)[0]

    def settings_header(self, **kwargs):
        msg = self.bundle.get_message('settings-header')
        if not msg or not msg.value:
            return f'[missing: settings-header]'
        return self.bundle.format_pattern(msg.value, kwargs)[0]

    def start_command_answer(self, **kwargs):
        msg = self.bundle.get_message('start-command-answer')
        if not msg or not msg.value:
            return f'[missing: start-command-answer]'
        return self.bundle.format_pattern(msg.value, kwargs)[0]

    def welcome(self, **kwargs):
        msg = self.bundle.get_message('welcome')
        if not msg or not msg.value:
            return f'[missing: welcome]'
        return self.bundle.format_pattern(msg.value, kwargs)[0]

    def welcome_user(self, **kwargs):
        msg = self.bundle.get_message('welcome-user')
        if not msg or not msg.value:
            return f'[missing: welcome-user]'
        return self.bundle.format_pattern(msg.value, kwargs)[0]
