class FieldGroup:
    """
    FieldGroup is a collection of related Fields on a page
    It collects and stores the data from the Field objects

    name is the key value in the dict
    """
    def __init__(self, name):
        self.fields = []
        self.result = {}
        self.name = name

    def add_field(self, field):
        self.fields.append(field)
        return self

    def extract_data(self):
        if (len(self.fields) > 0):
            for field in self.fields:
                self.result[field.get_name()] = field.get_data()
        return self

    def print_data(self):
        print(self.result)
        return self

    def get_data(self):
        return self.result

    def get_name(self):
        return self.name
