import random

sample = int(1000000)

damageGA = 0
damageGS = 0
damageRapier = 0
damageGWFGA = 0
damageGWFGS = 0
DuelingRapier = 0

def greatWeaponFighting(number):
    if number < 3:
        return 3
    else:
        return number
    
def greatWeaponFightingV2(number, dieSize):
    if number < dieSize / 2:
        return dieSize / 2 + 2
    else:
        return number

for j in range(sample):
    divineFavor = (random.randint(1,4))
    divineSmiteRoll1 = (random.randint(1,8))
    divineSmiteRoll2 = (random.randint(1,8))


    damageGS += (random.randint(1,6) + (random.randint(1,6)))
    damageGA += (random.randint(1,12))
    damageRapier += (random.randint(1,8))

    
    GWFGAroll = (random.randint(1,12))
    damageGWFGA += greatWeaponFighting(GWFGAroll)
    # damageGWFGA += greatWeaponFighting(divineFavor)
    if ( j % 5 == 0): 
        damageGWFGA += greatWeaponFighting(divineSmiteRoll1)
        damageGWFGA += greatWeaponFighting(divineSmiteRoll2)
        


    GWFGSroll1 = (random.randint(1,6))
    GWFGSroll2 = (random.randint(1,6))
    damageGWFGS += greatWeaponFighting(GWFGSroll1)
    damageGWFGS += greatWeaponFighting(GWFGSroll2)
    # damageGWFGS += greatWeaponFighting(divineFavor)
    if ( j % 5 == 0): 
        damageGWFGS += greatWeaponFighting(divineSmiteRoll1)
        damageGWFGS += greatWeaponFighting(divineSmiteRoll2)


    DuelingRapier += (random.randint(1,8) + 2)




percent = damageGA/damageGS

# print('percentage: ' + str(percent))
print('GreatAxe            damage: ' + str(damageGA))
print('GreatAxe with GWF   damage: ' + str(damageGWFGA))
print("Additional Damage         : " + str(damageGWFGA - damageGA), end="\n\n")

print('GreatSword          damage: ' + str(damageGS))
print('GreatSword with GWF damage: ' + str(damageGWFGS))
print("Additional Damage         : " + str(damageGWFGS - damageGS), end="\n\n")

print('rapier              Damage: ' + str(damageRapier))
print('dueling      Rapier Damage: ' + str(DuelingRapier))
print('Additional Damage         : ' + str(DuelingRapier - damageRapier), end="\n\n")

# print('percent of regular gs and regular rapier: ' + str(damageRapier/damageGS))
# print('percent of regular gs and dueling rapier: ' + str(DuelingRapier/damageGS))
