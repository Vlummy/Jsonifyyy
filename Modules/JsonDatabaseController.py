import json


class JsonDatabaseController(object):
    """Controller class for employee_dbs.json"""

    def __init__(self):
        """Constructor"""

    @staticmethod
    def json_to_list(path):
        with open(path) as data_file:
            json_file = json.loads(data_file.read())
        return json_file


    @staticmethod
    def write__to_json(current_json_objects, attribute_list, path):
        print(len(attribute_list))
        cleandb = open(path, 'w').close()
        dbs = open(path, "a")
        dbs.write('[')
        for obj in current_json_objects:
            text = list(str(obj))
            new_text = []
            for char in text:
                if char == "'":
                    char = '"'
                    new_text.append(char)
                else:
                    new_text.append(char)
            dbs.write("".join(new_text) + ", ")

        dbs.write('{')
        i = 0
        for attributes in attribute_list:
            dbs.write('"' + attributes.get_key() + '"' + ":" + '"' + attributes.get_value() + '"')
            i = i + 1
            if i != len(attribute_list):
                dbs.write(", ")
        dbs.write("}]")
        dbs.close()