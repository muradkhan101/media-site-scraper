from Field import Field
class FieldGroup:
    """
    A collection of field objects that will be processed
    """
    def __init__(self, fieldList, processEach):
        self.fieldList = fieldList
        self.processEach = processEach
        self.data = []

    def processList(self):
        for el in self.fieldList:
            if isinstance(el, FieldGroup):
                el.processList()
            else:
                try:
                    el.findOne().processResult()
                except:
                    print("Couldn't find element for", el.getName())
            
