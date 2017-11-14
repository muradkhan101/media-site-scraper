class Page:
    def __init__(self, handle, whenDone):
        """
        Describes layout of information you want to scrape on a page

        index is the index we are processing in fieldGroups
        handle is the Selenium tab handle
        """
        self.index = 0
        self.fieldStructures = []
        self.handle = handle
        self.whenDone = whenDone

    def addStructure(self, structure):
        self.fieldStructures.push(structure)
        return self

    def getStructures(self):
        return self.fieldStructures

    def done(self):
        self.whenDone()
