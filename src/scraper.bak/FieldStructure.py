class FieldStructure:
    """
    Class to hold all the Field queries for a page
    """
    def __init__(self):
        self.structure = {}

    # {
    #   "videos" : {
    #                "main": fieldGroup
    #                "children" : None
    #
    #
    #
    def addQuery(self, field, name, count = False):
        self.queries.push({
            "field" : field,
            "name" : name,
            "count": False
        })
        return self

    def removeQuery(self, name):
        self.queries = list(filter( lambda x : x["name"] != name, self.queries))
        return self

    def doQueries(self):
        return list(map(lambda x : {
            "name": result,
            "result": x["field"].findAll().processResult()
                 if x["count"]
                 else x["field"].findOne().processResult()},
                 self.queries))
