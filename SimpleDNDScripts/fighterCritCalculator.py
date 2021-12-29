# this program calculates how much damage a fighter would do vs a revised version
# of the fighter found online.


import random

dice1 = []
dice2 = []
highDice = []
lowDice = []
sample = int(1000000)
diceSize = 20
weaponDice = 12         # greataxe
superiorityDice = 8


for i in range(sample):
    dice1.append(int(random.random()*100) % diceSize + 1)
    dice2.append(int(random.random()*100) % diceSize + 1)

neededToHit = 0
totalHits = 0
averageHits = 0
damage = 0


for i in range(sample):         # normal criticals
    if dice1[i] == 20:
        damage += ((int(random.random()*100 % weaponDice + 1))*2)
print('Crit range 20 damage: ', end="")
print('{:>30}'.format(str(damage)))
damage = 0

for i in range(sample):         # fighter crit range 20-19
    if dice1[i] == 20 or dice1[i] == 19:
        damage += ((int(random.random()*100 % weaponDice + 1))*2)
print('Crit range 20-19 damage: ', end='')
print('{:>27}'.format(str(damage)))
damage = 0

for i in range(sample):         # revised fighter crit range 20-19 only use s.d. on 19 s.d. is not doubled
    if dice1[i] == 20:
        damage += ((int(random.random()*100 % weaponDice + 1))*2)

    elif dice1[i] == 19:
        damage += ((int(random.random()*100 % weaponDice + 1))*2) + (int(random.random()*100 % superiorityDice + 1))

print('Crit range 20 19 on S.D. no (S.D.)2 damage: ', end='')
print('{:>8}'.format(str(damage)))
damage = 0

for i in range(sample):         # revised fighter crit range 20-19 only use s.d. on 19 s.d. is doubled
    if dice1[i] == 20:
        damage += ((int(random.random()*100 % weaponDice + 1))*2)

    elif dice1[i] == 19:
        damage += (int(random.random()*100 % weaponDice + 1))*2 + (int(random.random()*100 % superiorityDice + 1))*2

print('Crit range 20 19 on S.D. (S.D.)2 damage: ', end='')
print('{:>11}'.format(str(damage)))
damage = 0



































# page end
