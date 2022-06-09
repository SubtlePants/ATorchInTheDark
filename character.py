
class character(object):
    def __init__(self):
        self.name = ""
        self.stress = 0
        self.corruption = 0
        self.corruptioncap = 5
        self.xp = 0
        self.skills = []
        self.conditions = []
        self.stash = 0
        self.companions = {}
        self.inventory = {}

    def addcondition(self, name):
        self.conditions.append(name)

    def addstress(self, stress):
        self.stress += stress
        if self.stress >= 6:
            self.addcorruption()
            self.stress = 0

    def addcorruption(self):
        self.corruption += 1

    def ressurect(self):
        self.conditions = []
        self.stress = 0
        self.corruption = 0
        self.corruptioncap -= 1