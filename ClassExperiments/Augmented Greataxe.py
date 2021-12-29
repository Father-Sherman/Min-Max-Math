import random
from PlayerCharacter import PC



def report(percent, GADamage, GSDamage):
    print('percentage: ' + str(percent))
    print('GreatAxe damage: ' + str(GADamage))
    print('GreatSword damage: ' + str(GSDamage))

def combat():
    GAOrc = PC(0, "balancedGA")
    GSOrc = PC(0, "GS")
    sample = int(1000000)
    for j in range(sample):
        GAOrc.Attack(GSOrc)
        GSOrc.Attack(GAOrc)
    percent = GSOrc.getDamageTaken()/GAOrc.getDamageTaken()
    report(percent, GSOrc.getDamageTaken(), GAOrc.getDamageTaken())

def main():
    combat()


main()
