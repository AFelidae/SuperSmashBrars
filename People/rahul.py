import random
from character import Character

class Rahul(Character):
    def __init__(self):
        super().__init__("Rahul", title="The Fried Tunak", hp=1500, attack=160, dodge=40, crit=40, defense=30,
                         gender=0, critValue=2)
        self.srec = 4
    def passive(self):
        if self.doescrit > 1:
            self.srec = self.srec/2
        if self.doesdodge == 0:
            self.srec = self.srec/2

    def special(self):
        pass


    def midround(self):
        if self.isSpecial:
            for stats, mods in self.enemy.modifiers.items():
                for key, values in mods.items():
                    if values > 1:
                        self.enemy.modifiers[stats][key] = 1 if "mult" in key else 0
            self.resource -= self.srec


    def passiveend(self):
        if self.doescrit > 1 and self.srec < 4:
            self.srec = 2*self.srec
        if self.doesdodge == 0 and self.srec < 4:
            self.srec = 2*self.srec

    def endround(self):
        super().endround()

            