import random
from character import Character

class Yash(Character):
    def __init__(self):
        super().__init__("Yash", title="TikTokThot", hp=1600, attack=170, dodge=20, crit=10, defense=10,
                         gender=0, critValue=2)
        self.srec = 1
        self.scount = -1
        self.turncount = 0
        self.buffs = ["hp", "attack", "defense", "crit", "dodge"]

    def passive(self):
        if self.turncount%3 == 0 and self.turncount != 0: 
            stat = random.randint(0,4)
            print("BLM, ACAB, CAL 2025")
            print("({}) was increased by 10%".format(self.buffs[stat]))

            if stat == 0:
                self.modifiers[self.buffs[stat]]['selfadd'] += 160
            elif stat < 3 and stat > 0:
                self.modifiers[self.buffs[stat]]['selfmult'] += 0.1
            else: 
                self.modifiers[self.buffs[stat]]['selfadd'] += 10
                
    def special(self):
        self.enemy.isParalyzed = True
        self.scount = 2
        self.resource -= self.srec
        self.srec += 2

    def endround(self):
        if self.scount > 0:
            self.scount -= 1
        if self.scount == 0:
            self.enemy.isParalyzed = False
            self.scount -= 1
        self.turncount += 1
        super().endround()
