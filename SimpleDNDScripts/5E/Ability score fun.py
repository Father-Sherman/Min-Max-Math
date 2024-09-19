import random


print('The standard array gives ' + str(15 + 14 + 13 + 12 + 10 + 8) + ' ability score points.')

asiRolls = 100000


threeDSixesTotal = 0
threeDSixesDropLowestTotal = 0

def roll(diceSize):         #returns a d6 roll
    return random.randint(1, diceSize)

for i in range(asiRolls):           #figures averages of rolling 3d6 per asi
    for j in range(18):
        threeDSixesTotal += roll(6)

threeDSixesAverage = threeDSixesTotal / asiRolls
print('Rolling 3d6 per asi gives ' + str(round(threeDSixesAverage, 1)) + ' ability score points.')


fourDSixesDropOne = []
fourDSixesDropOneTotal = 0

for i in range(asiRolls):           # figures averages of rolling 4d6 and droping the lowest per asi
    for j in range(6):
        fourDSixesDropOne = [roll(6), roll(6), roll(6), roll(6)]
        fourDSixesDropOneTotal += sum(fourDSixesDropOne) - min(fourDSixesDropOne)

fourDSixesDropOneAverage = fourDSixesDropOneTotal / asiRolls
print('Rolling 4d6 minus the lowest per asi gives ' + str(round(fourDSixesDropOneAverage, 1)) + ' ability score points.')


fourDSixes = []
fourDSixesTotal = 0

for i in range(asiRolls):           # figures averages of rolling 4d6 and droping the lowest per asi
    for j in range(6):
        fourDSixes = [roll(6), roll(6), roll(6), roll(6)]
        fourDSixesTotal += sum(fourDSixes)

fourDSixesAverage = fourDSixesTotal / asiRolls
print('Rolling 4d6 per asi gives ' + str(round(fourDSixesAverage, 1)) + ' ability score points.')


StatBlock_1 = 0
StatBlock_2 = 0

Advantage4d6d1_1 = []
Advantage4d6d1_2 = []

Advantage4d6d1Total = 0

for i in range(asiRolls):           # figures averages of rolling 4d6 and droping the lowest per asi
    for j in range(6):
        Advantage4d6d1_1 = [roll(6), roll(6), roll(6), roll(6)]
        StatBlock_1 += sum(Advantage4d6d1_1) - min(Advantage4d6d1_1)


    for j in range(6):
        Advantage4d6d1_2 = [roll(6), roll(6), roll(6), roll(6)]
        StatBlock_2 += sum(Advantage4d6d1_2) - min(Advantage4d6d1_2)

    if StatBlock_1 > StatBlock_2:
        Advantage4d6d1Total += StatBlock_1
    elif StatBlock_2 > StatBlock_1:
        Advantage4d6d1Total += StatBlock_2
    else:
        Advantage4d6d1Total += StatBlock_2

    StatBlock_1 = 0
    StatBlock_2 = 0


Advantage4d6d1Average = Advantage4d6d1Total / asiRolls
print('Rolling two sets of 4d6 minus the lowest and taking the higher set gives ' + str(round(Advantage4d6d1Average, 1)) + ' ability score points.')
