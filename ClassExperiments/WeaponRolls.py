import random
from DiceRolls import rollD6, rollD12

def getGARoll():
    return rollD12()

def getGSRoll():
    return(rollD6() + rollD6())

def getBalancedGARoll():
    GARoll = rollD12()
    if (GARoll == 12):
        GARoll = 18
    return GARoll
