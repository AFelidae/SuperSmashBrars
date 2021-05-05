import random
from character import Character

class Michael(Character):
    def __init__(self):
        super().__init__("Michael", title="Simply Milky", hp=2200, attack=180, dodge=10, crit=10, defense=10,
                         gender=0, critValue=2)
        self.srec = 1

    def passive(self):
        print(self.enemy)

    def special(self):
        self.enemy.forceSwapped = True
        
        print("player 2 swaps")

    def passiveend(self):
        if self.enemy.swappedin:
            self.enemy.modifiers['attack']['othermult'] = 0.8
            self.enemy.modifiers['defense']['othermult'] = 0.8
            self.enemy.modifiers['crit']['othermult'] = 0.8
            self.enemy.modifiers['dodge']['othermult'] = 0.8

    def endround(self):
        super().endround()