# this script compares the feat Great weapon master to Savage Attacker

# results: SA is obvously always better than normal damage GWM still has a 
# trade off around AC 20 where it gets worse than normal damage.
# to sum up, the benefits of GWM get worse as AC gets higher. 

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
damageDie = 12
improvedDivineSmiteDie = 8
damage = 0
damageSA = 0
damageGWM = 0
attackModGWM = -5
damageModGWM = 10


for i in range(13,25):

    for j in range(sample):
        if dice1[j] + strMod + profMod >= (i+1):
            totalHits += 1
            # remove the improved define smite damage here to compare
            damage += int((random.random()*100) % damageDie + 1) + strMod
        else:
            totalHits += 0
    averageHits = (totalHits/sample) * 100



    for j in range(sample):
        if dice1[j] + strMod + profMod >= (i+1):
            totalHits += 1
            # remove the improved define smite damage here to compare
            damageSA += max(int((random.random()*100) % damageDie + 1) + strMod, int((random.random()*100) % damageDie + 1) + strMod)
        else:
            totalHits += 0
    averageHits = (totalHits/sample) * 100





    for j in range(sample):
        if dice1[j] + strMod + profMod + attackModGWM >= (i + 1):
            totalHitsGWM += 1
            # remove the improved define smite damage here to compare
            damageGWM += int((random.random() * 100) % damageDie + 1) + strMod + damageModGWM
        else:
            totalHitsGWM += 0
    averageHitsGWM = (totalHitsGWM / sample) * 100




    print('{:>18}'.format('Needed To Hit: ' + str(i+1)), end='')
    # print('{:>25}'.format("  Chance to hit: %" + str(round(averageHits, 1))), end='')
    print('{:>20}'.format("  Damage: " + str(round(damage, 1))), end='')
    print('{:>20}'.format("  Damage SA: " + str(round(damageSA, 1))), end='')
    # print('{:>30}'.format("  Chance to hit GWM: %" + str(round(averageHitsGWM, 1))), end='')
    print('{:>22}'.format("  Damage GWM: " + str(round(damageGWM, 1))), end='')
    print('{:>35}'.format("  Additional GWM damage: " + str(round(damageGWM - damageSA, 1))), end='')
    print('{:>20}'.format("  percentage: " + str(round(damageGWM / damageSA, 2))),"%", end='')
    print(' ' + str(i+1))

    damage = 0
    damageSA = 0
    damageGWM = 0

    totalHits = 0
    totalHitsGWM = 0


# take the attack modifier + 11 and that is about the tipping point: attack bonus 5. 5+11 = 16-17 is the tipping point.
# there is some variation with str vs prof being higher. just plug in the numbers to tell for sure.
