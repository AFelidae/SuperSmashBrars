import random
from character import Character

class Jessica(Character):
    def __init__(self):
        super().__init__("Jessica", title="Fisiks Queen", hp=2300, attack=140, dodge=20, crit=10, defense=10,
                         gender=1, critValue=2)
        self.srec = 0

    def passive(self):
        self.modifiers['attack']['selfadd'] = 5*self.resource
        self.modifiers['crit']['selfadd'] = 5*self.resource
        self.modifiers['dodge']['selfadd'] = 5*self.resource

    def special(self):
        self.enemy.hp -= 50*self.resource
        self.resource = 0

    def endround(self):
        super().endround()