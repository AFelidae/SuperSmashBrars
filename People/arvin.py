import random
from character import Character

class Arvin(Character):
    def __init__(self):
        super().__init__("Arvin", title="The Vegetarian", hp=2000, attack=160, dodge=10, crit=20, defense=20,
                         gender=0, critValue=2)
        self.srec = 1

    def passive(self):
        o = random.randint(40, 60)
        self.modifiers['hp']['selfadd'] += o
        #self.hp = min(2100, self.hp + o)
        
        print("({}) heals {} health".format(self.name, o))

    def special(self):
        self.modifiers['attack']['selfadd'] += 20*self.resource
        print(self.attack)
        self.resource -= self.resource


    def endround(self):
        super().endround()

class Arvin2(Character):
    def __init__(self):
        super().__init__("Hat", title="TBA", hp=1500, attack=200, dodge=10, crit=10, defense=20,
                         gender=0, critValue=2)
        self.srec = 0
        self.enterFirstShift = False
        self.enterSecondShift = False
        self.secondShiftCount = 0
        self.secondShiftMax = 10
        self.savedHP = 0

    def firstShift(self, Mult):
        self.modifiers['attack']['selfmult'] *= Mult
        self.hp -= 150*(Mult-1)
        if self.hp <= 0:
            print("Great Job Arvin You Killed Yourself")
            self.modifiers['attack']['selfmult'] = 0
            self.resource = 0
        self.enterFirstShift = True

    def secondShift(self, Turns):
        print("Arvin has entered second shift for "+str(Turns)+" amount of turns")
        self.savedHP = self.getHP()
        self.secondShiftCount = Turns
        self.modifiers['attack']['selfmult'] *= 1/(Turns+1)
        self.enterSecondShift = True

    def passive(self):
        print(((((1-(self.getHP()/2400))*100) + self.getActualATK())*(self.resource/4)))
        if self.enterSecondShift == False:
            shift = int(input("Would you like to use first(1), second(2), or no shift(0): "))
            while shift != 0 and shift != 1 and shift != 2:
                shift = int(input("Please choose a shift: "))
            if shift == 1:
                mult = int(input("Enter Attack Mult: "))
                self.firstShift(mult)
            if shift == 2:
                turns = int(input(str(self.secondShiftMax)+" turns avaliable. Enter Invincibilty Turn Count: "))
                while turns > self.secondShiftMax:
                    turns = int(input("You can't stay Invincible for that long. "+str(self.secondShiftMax)+" turns avaliable. Please choose amount of turns: "))
                self.secondShift(turns)
            if shift == 0:
                pass
        else:
            print("Second shift lasts for "+str(self.secondShiftCount)+" amount of turns")
 
    def special(self):
        self.enemy.hp -= ((((1-(self.getHP()/2400))*100) + self.getActualATK())*(self.resource/4))
        print(((((1-(self.getHP()/2400))*100) + self.getActualATK())*(self.resource/4)))
        self.resource = 0

    def passiveend(self):
        if self.secondShiftCount > 0:
            self.hp = self.savedHP
            self.secondShiftMax -= 1
            self.secondShiftCount -= 1
        if self.secondShiftCount == 0:
            self.enterSecondShift = False


    def endround(self):
        if self.enterFirstShift == True:
            self.modifiers['attack']['selfmult'] = 1
            self.enterFirstShift = False
        super().endround()























