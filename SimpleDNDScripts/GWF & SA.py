# The purpose of this script is to compare vanilla GreatAxe with vanilla
# GreatSword in how their damage output scales with the Great Weapon fighter
# and Savage attacker feats

import random


def main():
    sample = int(1000000)
    damageGA = 0
    damageGS = 0
    GWFSAGA = 0
    GWFSAGS = 0
    damageGA, damageGS, GWFSAGA, GWFSAGS = doMath(sample, damageGA, damageGS,
                                                  GWFSAGA, GWFSAGS)
    percent = damageGA / damageGS
    report(percent, damageGA, GWFSAGA, damageGS, GWFSAGS)


# doMath() rolls one attack for GS and GA a lot of times
def doMath(sample, damageGA, damageGS, GWFSAGA, GWFSAGS):
    for j in range(sample):
        # adds vanilla damage to counters
        damageGA += (random.randint(1, 12))
        damageGS += (random.randint(1, 6) + (random.randint(1, 6)))

        # adds GWFSAGA damage to counter
        GWFGAroll1 = (random.randint(1, 12))
        GWFGAroll2 = (random.randint(1, 12))
        if (GWFGAroll1 < 3):
            GWFGAroll1 = (random.randint(1, 12))
        if (GWFGAroll2 < 3):
            GWFGAroll2 = (random.randint(1, 12))
        GWFSAGA += max(GWFGAroll1, GWFGAroll2)

        # adds GWFSAGS damage to counter
        GWFGSroll1 = (random.randint(1, 6))
        GWFGSroll2 = (random.randint(1, 6))
        GWFGSroll3 = (random.randint(1, 6))
        GWFGSroll4 = (random.randint(1, 6))
        if (GWFGSroll1 < 3):
            GWFGSroll1 = (random.randint(1, 6))
        if (GWFGSroll2 < 3):
            GWFGSroll2 = (random.randint(1, 6))
        if (GWFGSroll3 < 3):
            GWFGSroll3 = (random.randint(1, 6))
        if (GWFGSroll4 < 3):
            GWFGSroll4 = (random.randint(1, 6))
        GWFSAGS += max((GWFGSroll1 + GWFGSroll2), (GWFGSroll3 + GWFGSroll4))
    return damageGA, damageGS, GWFSAGA, GWFSAGS


# prints the results of doMath() in a human friendly way
def report(percent, damageGA, GWFSAGA, damageGS, GWFSAGS):
    '''
    dock string
    Author Brad
    '''
    print('percentage: ' + str(percent))
    print('GreatAxe                 damage: ' + str(damageGA))
    print('GreatAxe with GWF and SA damage: ' + str(GWFSAGA))
    print("percentage              : " + str(GWFSAGA / damageGA))
    print()
    print('GreatSword                 damage: ' + str(damageGS))
    print('GreatSword with GWF and SA damage: ' + str(GWFSAGS))
    print("percentage              : " + str(GWFSAGS / damageGS))


main()
