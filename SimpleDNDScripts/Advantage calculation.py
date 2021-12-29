# this script looks at hit chances for advantage

import random

dice1 = []
dice2 = []
highDice = []
lowDice = []
sample = int(1000000)
diceSize = 20


for i in range(sample):
    dice1.append(int((random.random()*100) % diceSize + 1))
    dice2.append(int((random.random()*100) % diceSize + 1))


average = 0
total = 0
hAverage = 0
hTotal = 0
lAverage = 0
lTotal = 0
crits = 0
neededToHit = 0
totalHits = 0
averageHits = 0
advantageHits = 0
disadvantageHits = 0
additional = []
less = []
averageAdditional = 0
averageLess = 0


for i in range(20):
    print('{:>6}'.format('AC: ' + str(i+1)), end='')
    for j in range(sample):
        if dice1[j] >= (i+1):
            totalHits += 1
        else:
            totalHits += 0
    averageHits = (totalHits/sample) * 100
    print('{:>8}'.format("%" + str(round(averageHits, 1))), end='')

    totalHits = 0
    for j in range(sample):
        if dice1[j] >= (i+1) or dice2[j] >= (i+1):
            totalHits += 1
        else:
            totalHits += 0
    advantageHits = (totalHits/sample) * 100
    additional.append(round((advantageHits - averageHits) / 5, 3))
    print('{:>20}'.format("   Advantage %" + str(round(advantageHits, 1))), end='')
    print('{:>7}'.format(" + "), end='')
    print('{:.2f}'.format(additional[i]), end='')
    advantageHits = 0

    totalHits = 0
    for j in range(sample):
        if dice1[j] >= (i+1) and dice2[j] >= (i+1):
            totalHits += 1
        else:
            totalHits += 0
    disadvantageHits = (totalHits/sample) * 100
    less.append(round((disadvantageHits - averageHits) / 5, 3))
    print('{:>23}'.format("   Disadvantage %" + str(round(disadvantageHits, 1))), end='   ')
    print('{:.2f}'.format(less[i]))

    totalHits = 0


for i in range(sample):
    total += dice1[i]
    if dice1[i] > dice2[i]:
        hTotal += dice1[i]
        lTotal += dice2[i]

    elif dice1[i] < dice2[i]:
        hTotal += dice2[i]
        lTotal += dice1[i]

    else:
        hTotal += dice1[i]
        lTotal += dice1[i]

    # else:
    #     hTotal += dice2[i]
    #     lTotal += dice2[i]
    # if dice1[i] == 20 or dice1[i] == 19:# or dice2[i] == 20 or dice2[i] == 19:
    #     crits += 1

average = total/sample
hAverage = hTotal/sample
lAverage = lTotal/sample

averageAdditional = sum(additional) / len(additional)
averageLess = sum(less) / len(less)

print("\n averageAdditional: ", averageAdditional ," \n")
print("\n averageLess: ", averageLess ," \n")


print("total: " + str(total))
print('average: ' + str(average))
print('hAverage: ' + str(hAverage))
print('Additional average damage:' + str(hAverage - average))
print('lAverage: ' + str(lAverage))
print('crits: ' + str(crits))
print('crit %: ' + str((crits/10000)))
