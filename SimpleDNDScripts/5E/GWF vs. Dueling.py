import random

sample = int(1000000)

damageGA = 0
damageGS = 0
damageRapier = 0
GWFGA = 0
GWFGS = 0
DuelingRapier = 0


for j in range(sample):
    damageGA += (random.randint(1,12))
    damageGS += (random.randint(1,6) + (random.randint(1,6)))
    damageRapier += (random.randint(1,8))

    GWFGAroll = (random.randint(1,12))
    if (GWFGAroll < 3):
        GWFGAroll = (random.randint(1,12))
    GWFGA += GWFGAroll

    GWFGSroll1 = (random.randint(1,6))
    GWFGSroll2 = (random.randint(1,6))
    if (GWFGSroll1 < 3):
        GWFGSroll1 = (random.randint(1,6))
    if (GWFGSroll2 < 3):
        GWFGSroll2 = (random.randint(1,6))
    GWFGS += GWFGSroll1
    GWFGS += GWFGSroll2

    DuelingRapier += (random.randint(1,8) + 2)




percent = damageGA/damageGS

print('percentage: ' + str(percent))
print('GreatAxe          damage: ' + str(damageGA))
print('GreatAxe with GWF damage: ' + str(GWFGA))
print("percentage              : " + str(GWFGA / damageGA), end="\n\n")

print('GreatSword          damage: ' + str(damageGS))
print('GreatSword with GWF damage: ' + str(GWFGS))
print("percentage                : " + str(GWFGS / damageGS), end="\n\n")

print('rapier              Damage: ' + str(damageRapier))
print('dueling      Rapier Damage: ' + str(DuelingRapier))
print('percentage                : ' + str(DuelingRapier/damageRapier), end="\n\n")

print('percent of regular gs and regular rapier: ' + str(damageRapier/damageGS))
print('percent of regular gs and dueling rapier: ' + str(DuelingRapier/damageGS))
