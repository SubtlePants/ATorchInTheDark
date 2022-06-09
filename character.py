
class character(object):
    def __init__(self):
        self.name = ""
        self.stress = 0
        self.corruption = 0
        self.xp = 0
        self.skills = []
        self.conditions = []
        self.stash = 0
        self.companions = {}
        self.inventory = {}

    def addCondition(self, name):
        self.conditions.append(name)

    def addStress(self, stress):
        self.stress += stress
        if self.stress >= 6:
            self.addCorruption()
            self.stress = 0

    def addCorruption(self):
        self.corruption += 1