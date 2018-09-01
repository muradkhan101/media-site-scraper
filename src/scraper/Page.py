from ..helpers.manage_tabs import switch_tab, close_tab
class Page:
    """
    Maintains the status of a page open in Selenium

    handle is the Selenium tab handle
    whenDone is a function that is called after all the steps are performed
    """
    def __init__(self, handle, whenDone):
        self.status = False
        self.handle = handle
        self.whenDone = whenDone
        self.groups = []

    def add_group(self, group):
        self.groups.append(group)

    def process_group_data(self):
        for group in self.groups:
            group.extractData().printData()
        return self

    def close_page(self, driver, handle = None):
        switch_tab(driver, self.handle)
        close_tab(driver, handle)
