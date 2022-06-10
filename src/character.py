class Character(object):
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
        self.inventory = []

    def addcondition(self, name):
        self.conditions.append(name)

    def addstress(self, stress):
        self.stress += stress
        if self.stress >= 6:
            self.addcorruption()
            self.stress = 0

    def addcofrruption(self):
        self.corruption += 1

    def ressurect(self):
        self.conditions = []
        self.stress = 0
        self.corruption = 0
        self.corruptioncap -= 1

    def isdead(self):
        # If the number of conditions is less than the number of skills, return False
        if len(self.conditions) < len(self.skills):
            return False

        # If the character's corruption is less than the corruption cap, return False
        if self.corruption < self.corruptioncap:
            return False

        # If there is at least one lantern or torch in the inventory, return False
        for item in self.inventory:
            if item.name == 'Torch':
                return False
            if item.name == 'Lantern':
                return False
        return True


# Global functions

def new_character(name, skills, inventory):
    character = Character()
    character.name = name
    character.skills = skills
    character.inventory = inventory

    return character
