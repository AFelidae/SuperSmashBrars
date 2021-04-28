import random
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

from game import Fight # this triggers a fight from the last line of game.py, unrelated to the simulation

# for simulation
d = {"Phillip" : 0, "Jessica" : 0}
for _ in range(1000):
    game = Fight(Phillip(), Jessica(), False)
    d[game.run()] += 1

print(d) #prints number of losses for each character 
