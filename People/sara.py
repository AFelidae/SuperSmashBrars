from character import Character

class Sara(Character):
    def __init__(self):
        super().__init__("Sara", title="Saraline Hooey", hp=1600, attack=150, dodge=20, crit=10, defense=10,
                         gender=1, critValue=2)
        self.srec = 3
        self.scount = 0
        self.scenemy = " "

    def passive(self):      
        if self.enemy.title == "The Aloof Alpha Male":
            self.modifiers['crit']['selfadd'] += 2.5
        else:
            self.modifiers['crit']['selfadd'] += 5
                 
    
    def special(self):
        self.enemy.modifiers['defense']['otheradd'] -= 110
        self.scount = 5
        self.scenemy = self.enemy.title
        self.resource -= self.srec
        self.srec += 2
    
    
    """
    def onswap(self):
        self.modifiers['crit']['selfadd'] = 0
        self.crit = int(self.crit/2)
    
    """
    def endround(self):
        if self.scount > 0 and self.enemy.title == self.scenemy:
            self.enemy.modifiers['defense']['otheradd'] += 20
            self.scount -= 1

                
                
        
        """
        if self.isSpecial:
            self.enemy.modifiers['defense']['otheradd'] -= -100
        """
        super().endround()
        
       
       
