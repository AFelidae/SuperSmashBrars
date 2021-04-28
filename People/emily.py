import random
from character import Character

class Emily(Character):
    def __init__(self):
        super().__init__("Emily", title="2-Dimensional", hp=1500, attack=180, dodge=10, crit=20, defense=20,
                         gender=1, critValue=2)
        self.srec = 5

    def passive(self):
        if self.enemy.gender == 0:
            self.modifiers['attack']['selfmult'] = 1.5
        

    def special(self):
        self.modifiers['attack']['selfmult'] *= 3
        self.enemy.modifiers['dodge']['othermult'] = 0
        self.resource -= self.srec

    def endround(self):
        if self.isSpecial:
            self.enemy.modifiers['dodge']['othermult'] = 1
            self.modifiers['attack']['selfmult'] = self.modifiers['attack']['selfmult']/3
            self.hp = self.hp/10
        super().endround()