# compares advantage to a +5 attack bonus

import random

def rollDice(sample):
    dice1 = []
    dice2 = []
    diceSize = 20
    for i in range(sample):
        dice1.append(int((random.random()*100) % diceSize + 1))
        dice2.append(int((random.random()*100) % diceSize + 1))
    return dice1, dice2

def main():
    sample = int(100000)
    diceArray1, diceArray2 = rollDice(sample)

    neededToHit = 0
    totalHits = 0
    averageHits = 0
    advantageHits = 0
    disadvantageHits = 0
    additional = []
    less = []


    for i in range(25):
        # normal percentage to hit
        print('{:>6}'.format('AC: ' + str(i+1)), end='')
        for j in range(sample):
            if diceArray1[j] >= (i+1):
                totalHits += 1

            else:
                totalHits += 0
        averageHits = (totalHits/sample) * 100
        print('{:>8}'.format("%" + str(round(averageHits, 1))), end='')
        totalHits = 0

        # Disadvantage percentage to hit
        for j in range(sample):
            if diceArray1[j] >= (i+1) and diceArray2[j] >= (i+1):
                totalHits += 1
            else:
                totalHits += 0
        advantageHits = (totalHits/sample) * 100
        print('{:>20}'.format("   Disadvantage %" + str(round(advantageHits, 1))), end='')
        print('{:>7}'.format(" + "), end='')
        print('{:.2f}'.format(totalHits), end='')
        totalHits = 0

        # +5 percentage chance to hit
        for j in range(sample):
            if diceArray1[j] +5 >= (i+1) and diceArray2[j] +5 >= (i+1):
                totalHits += 1
            else:
                totalHits += 0
        advantageHits = (totalHits/sample) * 100
        print('{:>15}'.format("  +5 %" + str(round(advantageHits, 1))), end='')
        print('{:>7}'.format(" + "), end='')
        print('{:.2f}'.format(totalHits))


        # print(' totalHits/advanstageHits ', totalHits/advantageHits)
        totalHits = 0





main()
