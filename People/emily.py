import random
from character import Character

class Emily(Character):
    def __init__(self):
        super().__init__("Emily", title="2-Dimensional", hp=1300, attack=220, dodge=20, crit=20, defense=20,
                         gender=1, critValue=2)
        self.srec = 6

    def passive(self):
        if self.enemy.gender == 0:
            self.modifiers['attack']['selfmult'] = 1.5
        

    def special(self):
        self.modifiers['attack']['selfmult'] *= 3
        self.enemy.doesdodge = 1
        self.resource -= self.srec

    def endround(self):
        if self.isSpecial:
            self.modifiers['attack']['selfmult'] /= 3
            self.hp = self.hp/10 
        super().endround()
