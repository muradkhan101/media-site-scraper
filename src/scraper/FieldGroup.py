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
        self.children = []

    def add_field(self, field):
        """
        Add a field or a list of fields to the field group
        The "Field" type should be added
        """
        try:
            for item in field:
                self.fields.append(item)
        except TypeError: 
            self.fields.append(field)
        return self

    def extract_data(self):
        """
        Extract data from the fields and their children and place in object
        """
        if self.fields:
            for field in self.fields:
                self.result[field.get_name()] = field.get_data()
        
        if self.children:
            for field_group in self.children:
                self.result[field_group.get_name()] = field_group.extract_data()

        return self.result

    def print_data(self, depth = 0):
        """
        Print data from the field group recursively
        """
        print(self.result)
        return self

    def extract_json(self, func=print):
        """
        Extracts data from the field group and outputs it in JSON format
        """
        func("{")

        if self.fields:
            for i in range(len(self.fields)):
                if i != len(self.fields) - 1 or self.children:
                    func("'", self.fields[i].get_name(),
                         "': ", self.fields[i].get_result(), ",")
                else:
                    func("'", self.fields[i].get_name(),
                         "': ", self.fields[i].get_result())
                
        if self.children:
            for i in range(len(self.children)):
                if i != len(self.children) - 1:
                    func("'", self.children[i].get_name(),
                    "': ", self.children.extract_json(func), ",")
                else:
                    func("'", self.children[i].get_name(),
                    "': ", self.children.extract_json(func))

        func("}")

    def get_data(self):
        """
        Return data from field group
        """
        return self.result

    def get_name(self):
        """
        Return the name of the field group
        """
        return self.name

    def add_child(self, child):
        """
        Add a child or a list of children to the field group
        The children are expected to be other field groups
        """
        try:
            for item in child:
                self.children.append(item)
        except TypeError: 
            self.children.append(child)
        return self
