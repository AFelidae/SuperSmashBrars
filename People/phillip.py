from character import Character
class Phillip(Character):
    def __init__(self):
        super().__init__("Phillip", title="Erik Rygh", hp=1000, attack=200, dodge=50, crit=10, defense=10,
                         gender=0, critValue=2)
        self.srec = 4
        self.specialKill = False

    def passive(self):
        #print(self.team)
        if self.specialKill: # this happens in the passive and endround so that it doesn't circumvent kyles passive
            self.modifiers['attack']['selfmult'] *= 2
            print("Philips attack increased")
            self.specialKill = False
        
        if 1 in [p.gender for p in self.team]:
            self.modifiers['attack']['selfadd'] = 50
            self.modifiers['defense']['selfadd'] = 30
        else:
            self.modifiers['attack']['selfadd'] = 0
            self.modifiers['defense']['selfadd'] = 0

        if self.enemy.gender != 1:
            self.modifiers['dodge']['selfmult'] = 0.8
        else:
            self.modifiers['dodge']['selfmult'] = 1

        
        
        
    
    
    def special(self):
        pass
    
    def endround(self):
        if self.isSpecial and self.enemy.onDeath():
            self.specialKill = True
        super().endround()
        
        
