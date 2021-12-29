import DiceRolls
from WeaponRolls import getGARoll, getGSRoll, getBalancedGARoll

class PC:
    AC = 10
    Weapon = ""
    damageTaken = 0
    CD = ""

    def __init__(self, AC, Weapon, ChannelDivinity):
        self.AC = AC
        self.Weapon = Weapon
        self.CD = ChannelDivinity

    def Attack(self, target):
        attackRoll = self.getAttackRoll()
        if(attackRoll == 20):
            target.takeDamage(self.getDamageRoll())
        if(attackRoll >= target.getAC()):
            target.takeDamage(self.getDamageRoll())
        else:
            pass


    def getDamageRoll(self):
        if(self.Weapon == "GA"):
            return getGARoll()
        elif(self.Weapon == "balancedGA"):
            return getBalancedGARoll()
        elif(self.getWeapon() == "Fist"):
            return DiceRolls.rollD4()
        else:
            return getGSRoll()

    def takeDamage(self, damage):
        self.damageTaken += damage

    def getDamageTaken(self):
        return self.damageTaken

    def getAttackRoll(self):
        if(self.CD == "SacredWeapon"):
            return (DiceRolls.rollD20() + 5)
        if(self.CD == "OathOfVengance"):
            return max(DiceRolls.rollD20(), DiceRolls.rollD20())

    def getAC(self):
        return self.AC

    def getWeapon(self):
        return self.Weapon
