import random
from character import Character

class Arvin(Character):
    def __init__(self):
        super().__init__("Arvin", title="The Vegetarian", hp=2100, attack=170, dodge=10, crit=20, defense=20,
                         gender=0, critValue=2)
        self.srec = 1

    def passive(self):
        o = random.randint(40, 60)
        self.modifiers['hp']['selfadd'] += o
        #self.hp = min(2100, self.hp + o)
        
        print("({}) heals {} health".format(self.name, o))

    def special(self):
        self.modifiers['attack']['selfadd'] += 20*self.resource
        self.resource -= self.resource

    def endround(self):
        super().endround()