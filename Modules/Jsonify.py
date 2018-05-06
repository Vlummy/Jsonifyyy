from Modules.JsonDatabaseController import JsonDatabaseController
from Modules.ObjectAttribute import ObjectAttribute
from Modules.FileChooser import HandleJsonFile
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.config import Config
Config.set('graphics', 'height', '200')


class MainScreen(Screen):
    pass


class AnotherScreen(Screen):
    pass


class ScreenManagement(ScreenManager):
    pass


class Grid(GridLayout):
    pass


class AttributeField(TextInput):
    pass


jsonify = Builder.load_file('Modules\jsonify.kv')


class Jsonify(App):
    keys = []
    values = []

    def build(self):
        return jsonify

    def new_attribute(self):
        key = AttributeField(multiline=False)
        key.hint_text = "Key"
        value = AttributeField(multiline=False)
        value.hint_text = "Value"
        self.root.m_s.ids["attributes"].add_widget(key)
        self.root.m_s.ids["attributes"].add_widget(value)

        self.keys.append(key)
        self.values.append(value)

    def write_to_database(self):
        all_attributes = []
        current_json_objects = []
        path = HandleJsonFile.open_json_file()
        try:
            current_json_file = JsonDatabaseController.json_to_list(path)
            for obj in current_json_file:
                current_json_objects.append(obj)
        except Exception:
            print("current JSON file is empty. Writing your new json object to file")

        i = 0
        while i < len(self.keys):
            new_attribute = ObjectAttribute()
            new_attribute.set_key(self.keys[i].text)
            new_attribute.set_value(self.values[i].text)
            all_attributes.append(new_attribute)
            i = i + 1

        JsonDatabaseController.write__to_json(current_json_objects, all_attributes, path)
