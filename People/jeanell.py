import random
from character import Character

class Jeanell(Character):
    def __init__(self):
        super().__init__("Jeanell", title="Left The Chat", hp=3000, attack=240, dodge=10, crit=0, defense=40,
                         gender=1, critValue=2)
        self.srec = 11
        self.usedSpecial = False
        self.extraDamage = 0
        self.currenthp = 0

    def passive(self):
        self.extraDamage = random.randint(1, 4)
        self.currenthp = self.getHP()

    def special(self):
        if not self.usedSpecial:
            self.modifiers['attack']['selfmult'] = 3
            print("Jeanell is immune to taking damage this turn")
            self.usedSpecial = True
            self.resource -= self.srec
            self.srec = 100000000

    def endround(self):
        if self.isSpecial:
            self.hp = self.currenthp
            self.modifiers['attack']['selfmult'] = 1
        if self.extraDamage == 1:
            self.hp -= 2*(self.currenthp - self.getHP())
            print("Jeanell takes 3x damage")


        super().endround()