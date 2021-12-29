from PlayerCharacter import PC


def report(percent, DevotionDamageTaken, VenganceDamageTaken):
    print('percentage: ' + str(percent))
    print('Vengance damage: ' + str(DevotionDamageTaken))
    print('Devotion damage: ' + str(VenganceDamageTaken))

def combat():
    Vengance = PC(0, "GS", "OathOfVengance")
    Devotion = PC(0, "GS", "SacredWeapon")
    # Monk = PC(17, "Fist", "none")
    sample = int(1000000)
    for j in range(sample):
        Vengance.Attack(Devotion)
        # if((j % 10) == 0):
        #     pass
        # else:
        Devotion.Attack(Vengance)
        # Monk.Attack(Vengance)
    percent = Devotion.getDamageTaken()/Vengance.getDamageTaken()
    report(percent, Devotion.getDamageTaken(), Vengance.getDamageTaken())

def main():
    combat()


main()
