# this script shows when someone should use a great oversized longbow

import random

dice1 = []
sample = int(100000)
diceSize = 20


for i in range(sample):
    dice1.append(int((random.random()*100) % diceSize + 1))


totalHits = 0
totalHitsGOLB = 0
averageHits = 0
averageHitsGOLB = 0
strMod = 4 # Keothi Str
profMod = 3 # Keothi Prof
damageDie = 6
damage = 0
damageGOLB = 0
attackModGOLB = -5


for i in range(25):
    print('{:>18}'.format('Needed To Hit: ' + str(i+1)), end='')
    for j in range(sample):
        if dice1[j] + strMod + profMod >= (i+1):
            totalHits += 1
            damage += int((random.random()*100) % damageDie + 1) + int((random.random()*100) % damageDie + 1) + strMod
        else:
            totalHits += 0
    averageHits = (totalHits/sample) * 100
    print('{:>25}'.format("  Chance to hit: %" + str(round(averageHits, 1))), end='')
    print('{:>20}'.format("  Damage: " + str(round(damage, 1))), end='')

    for j in range(sample):
        if dice1[j] + strMod + profMod + attackModGOLB >= (i + 1):
            totalHitsGOLB += 1
            damageGOLB += int((random.random()*100) % damageDie + 1) + int((random.random()*100) % damageDie + 1) + int((random.random()*100) % damageDie + 1) + int((random.random()*100) % damageDie + 1) + strMod
        else:
            totalHitsGOLB += 0
    averageHitsGOLB = (totalHitsGOLB / sample) * 100
    print('{:>30}'.format("  Chance to hit GOLB: %" + str(round(averageHitsGOLB, 1))), end='')
    print('{:>22}'.format("  Damage GOLB: " + str(round(damageGOLB, 1))), end='')

    print('{:>35}'.format("  Additional GOLB damage: " + str(round(damageGOLB - damage, 1))), end='')
    print(' ' + str(i+1))

    damage = 0
    damageGOLB = 0

    totalHits = 0
    totalHitsGOLB = 0

# a rule of thumb on when to use two arrows is to take your attack bonus and add 8 to it. For example:
# Attack bonus 5. 5+8 = 13 When the enemies AC is 13 or lower you will do more damage using two arrows
# But if their AC is Greater than 13 you will do less damage with two arrows.
