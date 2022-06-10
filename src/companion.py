

class companion(object):
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self. harm = 0

    def isdead(self):
        if self.harm >= 2: return True
        return False

    def harm(self):
        self.harm += 1
