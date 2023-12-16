# this script shows when someone should use great weapon master

import random

dice1 = []
sample = int(100000)
diceSize = 20


for i in range(sample):
    dice1.append(int((random.random()*100) % diceSize + 1))


totalHits = 0
totalHitsGWM = 0
averageHits = 0
averageHitsGWM = 0
strMod = 4
profMod = 3
damageDie = 12
damage = 0
damageGWM = 0
attackModGWM = -5
damageModGWM = 10


for i in range(25):
    print('{:>18}'.format('Needed To Hit: ' + str(i+1)), end='')
    for j in range(sample):
        if dice1[j] + strMod + profMod >= (i+1):
            totalHits += 1
            damage += int((random.random()*100) % damageDie + 1) + strMod
        else:
            totalHits += 0
    averageHits = (totalHits/sample) * 100
    print('{:>25}'.format("  Chance to hit: %" + str(round(averageHits, 1))), end='')
    print('{:>20}'.format("  Damage: " + str(round(damage, 1))), end='')

    for j in range(sample):
        if dice1[j] + strMod + profMod + attackModGWM >= (i + 1):
            totalHitsGWM += 1
            damageGWM += int((random.random() * 100) % damageDie + 1) + strMod + damageModGWM
        else:
            totalHitsGWM += 0
    averageHitsGWM = (totalHitsGWM / sample) * 100
    print('{:>30}'.format("  Chance to hit GWM: %" + str(round(averageHitsGWM, 1))), end='')
    print('{:>22}'.format("  Damage GWM: " + str(round(damageGWM, 1))), end='')

    print('{:>35}'.format("  Additional GWM damage: " + str(round(damageGWM - damage, 1))), end='')
    print(' ' + str(i+1))

    damage = 0
    damageGWM = 0

    totalHits = 0
    totalHitsGWM = 0


# take the attack modifier + 11 and that is about the tipping point: attack bonus 5. 5+11 = 16-17 is the tipping point.
# there is some variation with str vs prof being higher. just plug in the numbers to tell for sure.
