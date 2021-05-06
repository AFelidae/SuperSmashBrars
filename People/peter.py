from character import Character
import random

class Peter(Character):
    def __init__(self):
        super().__init__("Peter", title="Thicc Booty", hp=2500, attack=160, dodge=20, crit=10, defense=25,
                         gender=0, critValue=2)
        self.srec = 0

    def passive(self):
        pass
    
    def special(self):
        for i in self.enemy.team:
            i.modifiers['attack']['othermult'] += -self.resource * 0.01
            i.modifiers['dodge']['othermult'] += -self.resource * 0.01
            i.modifiers['crit']['othermult'] += -self.resource * 0.01
            i.modifiers['defense']['othermult'] += -self.resource * 0.01
        
            print("{}'s stats dropped {}%!".format(self.enemy.name, self.resource))
        self.resource = 0
    
    def endround(self):
        if random.uniform(1, 100) <= 40:
            self.resource += 2 
            
        if self.doescrit != 1:
            self.resource += 3
        
        if self.doesdodge != 1:
            self.resource += 3  

        super().endround()
