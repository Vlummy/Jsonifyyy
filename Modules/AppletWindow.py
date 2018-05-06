from Modules.JsonDatabaseController import JsonDatabaseController
from Modules.ObjectAttribute import ObjectAttribute
from Modules.FileChooser import HandleJsonFile
from tkinter import *
from tkinter import ttk


class AppletWindow(Frame):
    keys = []
    values = []

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid(column=0, row=7, padx=20, pady=5)

        self.header_label = ttk.Label(text="JSON")
        self.header_label.grid(padx=10, pady=10)

        self.new_attribute = ttk.Button(self, text="New Attribute", command=self.new_input_field)
        self.new_attribute.grid(column=1, padx=10, pady=10)

        self.write_button = ttk.Button(self, text="Write to database", command=self.write_to_database)
        self.write_button.grid(column=1, padx=10, pady=10)

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
            new_attribute.set_key(self.keys[i].get())
            new_attribute.set_value(self.values[i].get())
            all_attributes.append(new_attribute)
            i = i + 1

        JsonDatabaseController.write__to_json(current_json_objects, all_attributes, path)

    def new_input_field(self):
        self.key_field = ttk.Entry(self)
        self.key_field.insert(0, "key")
        self.key_field.grid(column=0, row=(len(self.keys)), padx=10, pady=10)
        self.value_field = ttk.Entry(self)
        self.value_field.insert(0, "value")
        self.value_field.grid(column=2, row=(len(self.keys)), padx=10, pady=10)

        self.keys.append(self.key_field)
        self.values.append(self.value_field)


root = Tk()
window = AppletWindow(root)
root.mainloop()