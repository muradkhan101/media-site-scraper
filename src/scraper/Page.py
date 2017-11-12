class Page:
    def __init__(self, handle, whenDone):
        """
        Describes layout of information you want to scrape on a page

        index is the index we are processing in fieldGroups
        handle is the Selenium tab handle
        """
        self.index = 0
        self.fieldGroups = []
        self.handle = handle
        self.whenDone = whenDone

    def addGroup(self, group):
        self.fieldGroups.push(group)
        return self

    def getGroups(self):
        return self.fieldGroups

    def done(self):
        self.whenDone()

    
