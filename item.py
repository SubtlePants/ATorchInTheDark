
class Item(object):
    def __init__(self):
        self.name = ""
        self.load = 0
        self.description = ""

    def __init__(self, name, load, description):
        self.name = name
        self.load = load
        self.description = description

    def __init__(self, item):
        self.name = item.name
        self.load = item.load
        self.description = item.description

    def expend(self):
        # expend an item by reducing its load by 1
        self.load -= 1
