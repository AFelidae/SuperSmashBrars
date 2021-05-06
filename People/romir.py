from character import Character

class Romir(Character):
    def __init__(self):
        super().__init__("Romir", title="Prophet, Pimp, Maverick", hp=1200, attack=160, dodge=15, crit=15, defense=20,
                         gender=0, critValue=2)
        self.srec = 0
        self.canRespawn = True

    def passive(self):
        self.modifiers['attack']['selfadd'] = 10*self.resource
        self.modifiers['defense']['selfadd'] = 5*self.resource
        
    def special(self):
        pass

    def endround(self): 
        if self.canRespawn and self.getHP() < 0:
            self.hp = 1200
          
            print("THE PIMP RETURNS! {} respawned".format(self.name))
            self.canRespawn = False           
        super().endround()
