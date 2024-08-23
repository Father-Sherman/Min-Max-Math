# this script shows when someone should use great weapon master

import random

dice1 = []
sample = int(100000)
diceSize = 20


for i in range(sample):
    dice1.append(int((random.random()*100) % diceSize + 1))


averageHits = 0
averageHitsGWM = 0
strMod = 4
damageDie = 12
damage = 0
damageGWM5 = 0
damageGWM5_5 = 0
attackModGWM = -5
damageModGWM = 10


for i in range(6,25):

    # normal damage
    print('{:<14}'.format('To Hit: ' + str(i+1)), end='')
    # for j in range(sample):
    #     if dice1[j] + strMod + profMod >= (i+1):
    #         damage += int((random.random()*100) % damageDie + 1) + strMod

    # print('{:<18}'.format("  Damage: " + str(round(damage, 1))), end='')

    for k in range(2,7):
        # 5e GWM damage
        for j in range(sample):
            if dice1[j] + strMod + k + attackModGWM >= (i + 1):
                damageGWM5 += int((random.random() * 100) % damageDie + 1) + strMod + damageModGWM
                
        print('{:<17}'.format("PB" + str(k) + "  5e: " + str(round(damageGWM5, 1))), end='')

        # 5.5e GWM damage
        for j in range(sample):
            if dice1[j] + strMod + k >= (i + 1):
                damageGWM5_5 += int((random.random() * 100) % damageDie + 1) + strMod + k

        print('{:<16}'.format("  5.5e: " + str(round(damageGWM5_5, 1))), end='')
        print('{:<12}'.format(" 5e " if damageGWM5 > damageGWM5_5 else " 5.5e " ), end='')

        damageGWM5_5 = 0
        damageGWM5 = 0






    # print('{:<26}'.format("  Difference: " + str(round(damageGWM5 - damage, 1))), end='')
    print(' ' + str(i+1))

    damage = 0

    totalHits = 0
    totalHitsGWM = 0


# take the attack modifier + 11 and that is about the tipping point: attack bonus 5. 5+11 = 16-17 is the tipping point.
# there is some variation with str vs prof being higher. just plug in the numbers to tell for sure.
