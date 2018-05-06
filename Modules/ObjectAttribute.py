class ObjectAttribute:
    """Employee is a class prototype for all employees and their attributes"""
    key = ""
    value = ""

    def __init__(self):
        """Constructor for this class"""

    def get_key(self):
        return self.key

    def get_value(self):
        return self.value

    def set_key(self, key):
        self.key = key

    def set_value(self, value):
        self.value = value

    def print_attribute(self):
        print("Key: ", self.get_key())
        print("Value: ", self.get_value())