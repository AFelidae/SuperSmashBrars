import random


class Character(object):
    # self.properties = {name : None, hp : None, attack : None, dodge : None, crit : None, defense : None, gender : None}
    def __init__(self, name, title, hp, attack, dodge, crit, defense, gender, critValue):
        self.name = name
        self.title = title
        self.hp = hp
        self.attack = attack
        self.dodge = dodge
        self.crit = crit
        self.defense = defense
        self.gender = gender
        self.resource = 0
        self.critValue = critValue
        
        self.doescrit = 1
        self.doesdodge = 0
        
        self.swappedin = False
        
        self.enemy = None
        self.team = None

        self.isParalyzed = False
        self.isSimping = False
        self.forceSwapped = False
        
        
        self.isSpecial = False
        
        self.modifiers = {'hp' :      {"selfmult" : 1, "othermult" : 1, "selfadd" : 0, "otheradd" : 0}, 
                        'attack' :    {"selfmult" : 1, "othermult" : 1, "selfadd" : 0, "otheradd" : 0},
                        'dodge' :     {"selfmult" : 1, "othermult" : 1, "selfadd" : 0, "otheradd" : 0}, 
                        'crit' :      {"selfmult" : 1, "othermult" : 1, "selfadd" : 0, "otheradd" : 0},
                        'defense' :   {"selfmult" : 1, "othermult" : 1, "selfadd" : 0, "otheradd" : 0},
                        'critValue' : {"selfmult" : 1, "othermult" : 1, "selfadd" : 0, "otheradd" : 0}}
                        
        """
        actualattack = attack * modifiers[attack][selfmult] * modifiers[attack][othermult] + modifiers[attack][selfadd]+ modifiers[attack][otheradd]
        actualdodge = dodge * modifiers[dodge][selfmult] * modifiers[dodge][othermult] + modifiers[dodge][selfadd]+ modifiers[dodge][otheradd]
        actualcrit = crit * modifiers[crit][selfmult] * modifiers[crit][othermult] + modifiers[crit][selfadd]+ modifiers[crit][otheradd]
        actualdefense = defense * modifiers[defense][selfmult] * modifiers[defense][othermult] + modifiers[defense][selfadd]+ modifiers[defense][otheradd]
        """
        
    def __str__(self):
        return("{}({})".format(self.name, self.hp))

    def startround(self):
        pass

    def midround(self):
        pass
        
    def passive(self):
        pass

    def passiveend(self):
        pass

    def special(self):
        pass

    def onSwapIn(self):
        pass
        
    def onSwapOut(self):
        pass
        
    def onDeath(self):
        if self.getHP() <= 0:
            return True
        
        

    def testdodged(self):
        self.doesdodge = 1 if random.uniform(1, 100) > self.getActualDODGE() else 0

    def testcrit(self):
        self.doescrit = self.critValue if random.uniform(1, 100) < self.getActualCRIT() else 1

    def damage(self, opponentattack, critmult):
        damage = None
        dodgemult = self.dodged()
        if self.defense > 0:
            damage = dodgemult * (max(0, critmult * opponentattack - self.defense))
        else:
            damage = dodgemult * (max(0, critmult * opponentattack - (2 * self.defense)))

        if critmult > 1:  # its greater than 1 because some characters will have a 3 crit multiplier
            print("Was dealt a critical hit")

        if dodgemult == 0:
            print("The attack was dodged")
        else:
            print("({}) took {} damage".format(self.name, damage))
        self.hp -= damage
     
    def getActualATK(self):
        return (self.attack + self.modifiers['attack']['selfadd'] + self.modifiers['attack']['otheradd']) * self.modifiers['attack']['selfmult'] * self.modifiers['attack']['othermult'] 
        
    def getActualDODGE(self):
        return (self.dodge + self.modifiers['dodge']['selfadd'] + self.modifiers['dodge']['otheradd']) * self.modifiers['dodge']['selfmult'] * self.modifiers['dodge']['othermult'] 
        
    def getActualCRIT(self):
        return (self.crit + self.modifiers['crit']['selfadd'] + self.modifiers['crit']['otheradd']) * self.modifiers['crit']['selfmult'] * self.modifiers['crit']['othermult'] 
        
    def getActualDEF(self):
        return (self.defense + self.modifiers['defense']['selfadd'] + self.modifiers['defense']['otheradd']) * self.modifiers['defense']['selfmult'] * self.modifiers['defense']['othermult'] 

    def getHP(self):
        return (self.hp + self.modifiers['hp']['selfadd'] + self.modifiers['hp']['otheradd']) * self.modifiers['hp']['selfmult'] * self.modifiers['hp']['othermult']

    def endround(self):
        self.resource += 1
        self.swappedin = False
        
        if self.isSpecial:
            self.isSpecial = False
