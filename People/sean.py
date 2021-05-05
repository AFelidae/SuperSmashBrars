from character import Character

class Sean(Character):
    def __init__(self):
        super().__init__("Sean", title="Long Dong Sean Fong", hp=1200, attack=160, dodge=33, crit=33, defense=20,
                         gender=0, critValue=2)
        self.srec = 3

    def passive(self):
        self.modifiers['crit']['selfadd'] += 3
        self.modifiers['dodge']['selfadd'] += 3
        
    
    
    def special(self):

        #self.modifiers['dodge']['selfmult'] = 100000
        #self.modifiers['crit']['selfmult'] = 100000
        self.doesdodge = 0
        self.doescrit = self.critValue 
        self.resource -= self.srec
    
    def endround(self):
        if self.isSpecial:
            self.modifiers['dodge']['selfmult'] = 1
            self.modifiers['crit']['selfmult'] = 1
            
        super().endround()
        
        
