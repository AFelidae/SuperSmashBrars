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
from People.kyle import Kyle
from People.jeanell import Jeanell

from game import Fight # this triggers a fight from the last line of game.py, unrelated to the simulation

gauntlet = {"Arvin": Arvin(), "Sean": Sean(), "Jessica": Jessica(), "Romir": Romir(), "Emily": Emily(), "Jay": Jay(), "Jeanell": Jeanell(), "Kyle": Kyle(), "Rahul": Rahul(), "Jiyang": Jiyang()}


d = {"Jiyang" : 0, "Jessica" : 0}  
for _ in range(1000):
	game = Fight(Jiyang(), Jessica(), False)
	d[game.run()] += 1

print(d)
'''
### I don't know why this doesn't work but it doesn't

for key, value in gauntlet.items():
	e = {"Arvin" : 0, key : 0}  
	for _ in range(1000):
		game = Fight(Arvin(), value, False)
		e[game.run()] += 1

	print(e) #prints number of losses for each character 

#run_the_gauntlet("Arvin", Arvin())


'''