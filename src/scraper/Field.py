class Field:
    """
    Class to extract data from a single selector on a page
    @params
    parent : parent element to query as root (default should be driver)
    by : By type from selenium.webdriver.common.by
    selector : class, id, tag name, etc. to query for
    """
    def __init__(self, parent, by, selector, name, single = True, process = lambda x : x):
        self.parent = parent
        self.by = by
        self.selector = selector
        self.name = name
        self.process = process
        self.single = single
        self.result = None

    def find_one(self):
        self.result = self.parent.find_element(self.by, self.selector)
        return self

    def find_all(self):
        self.result = self.parent.find_elements(self.by, self.selector)
        return self

    def get_data(self):
        if not self.result:
            self.findOne() if self.single else self.findAll()

        return (
            self.process(self.result)
            if type(self.result) is not list
            else list(map(lambda x: self.process(x)), self.result)
            )

    def get_result(self):
        return self.result

    def get_name(self):
        return self.name

    def setSelector(self, selector):
        self.selector = selector

    def setBy(self, by):
        self.by = by
