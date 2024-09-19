# this script shows when someone should use great weapon master and compairs 
# paladins 11th level ability improved devine smite which adds an aditional d8 
# of damage per hit

# results: in the other program just looking at GWM the output showed that the
# trade off point (for using GWM) for a character with maxes str and proficency 
# is between AC 21-22 when improved divine smite is added to the mix the trade off
# off point is dropped to 19-20 

import random

dice1 = []
sample = int(100_000)
diceSize = 20


for i in range(sample):
    dice1.append(int((random.random()*100) % diceSize + 1))


totalHits = 0
totalHitsGWM = 0
averageHits = 0
averageHitsGWM = 0
strMod = 5
profMod = 6
damageDie = 10
improvedDivineSmiteDie = 8
damage = 0
damageGWM = 0
attackModGWM = -5
damageModGWM = 10


for i in range(25):


    for j in range(sample):
        if dice1[j] + strMod + profMod >= (i+1):
            totalHits += 1
            # remove the improved define smite damage here to compare
            damage += int((random.random()*100) % damageDie + 1) + int((random.random()*100) % improvedDivineSmiteDie +1) + strMod
        else:
            totalHits += 0
    averageHits = (totalHits/sample) * 100





    for j in range(sample):
        if dice1[j] + strMod + profMod + attackModGWM >= (i + 1):
            totalHitsGWM += 1
            # remove the improved define smite damage here to compare
            damageGWM += int((random.random() * 100) % damageDie + 1) + int((random.random()*100) % improvedDivineSmiteDie +1) + strMod + damageModGWM
        else:
            totalHitsGWM += 0
    averageHitsGWM = (totalHitsGWM / sample) * 100




    print('{:>18}'.format('Needed To Hit: ' + str(i+1)), end='')
    print('{:>25}'.format("  Chance to hit: %" + str(round(averageHits, 1))), end='')
    print('{:>20}'.format("  Damage: " + str(round(damage, 1))), end='')
    print('{:>30}'.format("  Chance to hit GWM: %" + str(round(averageHitsGWM, 1))), end='')
    print('{:>22}'.format("  Damage GWM: " + str(round(damageGWM, 1))), end='')
    print('{:>35}'.format("  Additional GWM damage: " + str(round(damageGWM - damage, 1))), end='')
    print('{:>20}'.format("  percentage: " + str(round(damageGWM / damage, 2))),"%", end='')
    print(' ' + str(i+1))

    damage = 0
    damageGWM = 0

    totalHits = 0
    totalHitsGWM = 0


# take the attack modifier + 11 and that is about the tipping point: attack bonus 5. 5+11 = 16-17 is the tipping point.
# there is some variation with str vs prof being higher. just plug in the numbers to tell for sure.
