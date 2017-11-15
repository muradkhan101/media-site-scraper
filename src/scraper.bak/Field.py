class Field:
    """
    Class to query a single field on a page
    @params
    parent : parent element to query as root (default should be driver)
    by : By type from selenium.webdriver.common.by
    selector : class, id, tag name, etc. to query for
    """
    def __init__(self, parent, by, selector, process = lambda x : x, name):
        self.parent = parent
        self.by = by
        self.selector = selector
        self.process = process
        self.result = None
        self.name = name

    def findOne(self):
        self.result = self.parent.find_element(self.by, self.selector)
        return self

    def findAll(self):
        self.result = self.parent.find_elements(self.by, self.selector)
        return self

    def process(self):
        if (not self.result):
            self.findOne()

        return self.process(self.result) if type(self.result) is not list else list(map(lambda x: self.process), self.result)

    def getResult(self):
        return self.result

    def getName(self):
        return self.name

    def setSelector(self, selector):
        self.selector = selector

    def setBy(self, by):
        self.by = by
