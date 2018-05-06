from tkinter import filedialog
from tkinter import *


class HandleJsonFile:
    def __init__(self):
        """Constructor"""

    @staticmethod
    def open_json_file():
        root = Tk()
        root.withdraw()
        root.filename = filedialog.askopenfilename(initialdir="/",
                                                   title="Select file",
                                                   filetypes=(("json files", "*.json"), ("all files", "*.*")))
        return root.filename