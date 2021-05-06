import os
import random
import sys

from People.arvin import Arvin
from People.jay import Jay
from People.sean import Sean
from People.jiyang import Jiyang
from People.sara import Sara
from People.peter import Peter
from People.phillip import Phillip
from People.romir import Romir
from People.emily import Emily
from People.rahul import Rahul
from People.jessica import Jessica
from People.kyle import Kyle
from People.yash import Yash
from People.jeanell import Jeanell
#from People.arvin import Hat

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')  # There might be a way to do this only using sys not sure


# Restore
def enablePrint():
    sys.stdout = sys.__stdout__


class Fight(object):
    turn = 1

    def __init__(self, p1, p2, output):
        self.p1 = p1
        self.p2 = p2
        self.output = output

        self.p2.enemy = self.p1
        self.p1.enemy = self.p2
        self.run()



    # make universally probably
    def damage(self, attacker, victim):
        damage = None

        actualattack = attacker.getActualATK()
        actualdodge = victim.getActualDODGE()
        actualcrit = attacker.getActualCRIT()
        actualdefense = victim.getActualDEF()

        print(
            "Atk = {}\nDodge = {}\nCrit = {}\nDef = {}\n".format(actualattack, actualdodge, actualcrit, actualdefense))

        if actualdefense > 0:
            damage = victim.doesdodge * (max(0, attacker.doescrit * actualattack - actualdefense))
        else:
            damage = victim.doesdodge * (max(0, attacker.doescrit * actualattack - (2 * actualdefense)))

        if victim.doesdodge == 0:
            print("The attack was dodged")
        else:
            if attacker.doescrit > 1:  # its greater than 1 because some characters will have a 3 crit multiplier
                print("Was dealt a critical hit")
            print("({}) took {} damage".format(victim.name, damage))
        victim.hp -= damage

    def run(self):
        if not self.output:
            blockPrint()

        coinflip = random.randint(0, 1)
        if coinflip == 0:
            self.p1, self.p2 = self.p2, self.p1

        lose = None

        while True:
            print("TURN {}".format(self.turn))
            print("{}'s Resource count: {}".format(self.p1.name, self.p1.resource))
            print("{}'s Resource count: {}".format(self.p2.name, self.p2.resource))
            print("Player 1 ({}) HP: {}".format(self.p1.name, self.p1.getHP()))
            print("Player 2 ({}) HP: {}".format(self.p2.name, self.p2.getHP()))
 
            # death checks

            if self.p1.getHP() <= 0 and self.p2.getHP() <= 0:
                return "Draw"
                break

            elif self.p2.getHP() <= 0:
                lose = self.p2
                break

            elif self.p1.getHP() <= 0:
                lose = self.p1
                break

            self.p1.startround()
            self.p2.startround()

            # test to see if player will dodge and/or crit
            self.p1.testdodged()
            self.p2.testdodged()
            self.p1.testcrit()
            self.p2.testcrit()

            #start passives 
            self.p1.passive()
            self.p2.passive()

            # for normal mode simulation
            if self.output:
                p1c = input("{}: Select your move ({})".format(self.p1.name,
                                                               "a, s" if self.p1.resource >= self.p1.srec else "a"))
                p2c = input("{}: Select your move ({})".format(self.p2.name,
                                                               "a, s" if self.p2.resource >= self.p2.srec else "a"))
            else:
                p1c = 's'
                p2c = 's'
                if self.p1.title == "Fisiks Queen":
                    p1c = 'a'
                if self.p2.title == "Fisiks Queen":
                    p2c = 'a'

            if p1c.lower() == "s" and not self.p1.isParalyzed:
                if self.p1.resource >= self.p1.srec:
                    self.p1.isSpecial = True
                    self.p1.special()

            if p2c.lower() == "s" and not self.p2.isParalyzed:
                if self.p2.resource >= self.p2.srec:
                    self.p2.isSpecial = True
                    self.p2.special()


            self.p1.midround()
            self.p2.midround()
            # p1 attacks p2
            """
            print("({}) attacks ({})".format(self.p1.name, self.p2.name))

            p1.doescrit = 2 if random.uniform(1, 100) < self.p1.crit else 1
            self.p2.damage(self.p1.attack, doescrit)

            #p2 attacks p1
            print("({}) attacks ({})".format(self.p2.name, self.p1.name))

            p2.doescrit = 2 if random.uniform(1, 100) < self.p2.crit else 1
            self.p1.damage(self.p2.attack, doescrit)
            """
            if not self.p1.isParalyzed:
                print("({}) attacks ({})".format(self.p1.name, self.p2.name))
                self.damage(self.p1, self.p2)

            # p2 attacks p1
            if not self.p2.isParalyzed:
                print("({}) attacks ({})".format(self.p2.name, self.p1.name))
                self.damage(self.p2, self.p1)


            if self.p1.isParalyzed:
                print("({}) is Paralyzed and can't move".format(self.p1.name))
            if self.p2.isParalyzed:
                print("({}) is Paralyzed and can't move".format(self.p2.name))

            print("MODIFIERS")
            print(self.p1.modifiers)
            print(self.p2.modifiers)
            print("-----------------------------------")


            # end passives

            self.p1.passiveend()
            self.p2.passiveend()

            # This function should be removed
            # self.p1.specialend()
            # self.p2.specialend()

            self.p1.endround()
            self.p2.endround()

            self.turn += 1
            print("\n\n")

        print("{} loses!".format(lose.name))
        print("{} : {}\n{} : {}".format(self.p1.name, self.p1.hp, self.p2.name, self.p2.hp))
        enablePrint()
        return lose.name

if __name__ == "__main__":                   
    game = Fight(Rahul(), Sean(), True)

