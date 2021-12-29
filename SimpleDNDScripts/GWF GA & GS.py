import random

sample = int(1000000)

damageGA = 0
damageGS = 0
GWFGA = 0
GWFGS = 0


for j in range(sample):
    damageGS += (random.randint(1,6) + (random.randint(1,6)))
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

percent = damageGA/damageGS

print('percentage: ' + str(percent))
print('GreatAxe          damage: ' + str(damageGA))
print('GreatAxe with GWF damage: ' + str(GWFGA))
print("percentage              : " + str(GWFGA / damageGA))

print('GreatSword          damage: ' + str(damageGS))
print('GreatSword with GWF damage: ' + str(GWFGS))
print("percentage              : " + str(GWFGS / damageGS))
