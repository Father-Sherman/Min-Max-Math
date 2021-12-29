import random

sample = int(1000000)

SAGA = 0
GA = 0


for j in range(sample):
    roll1 = random.randint(1,12)
    roll2 = random.randint(1,12)
    SAGA += max(roll1, roll2)
    GA += random.randint(1,12)

percent = SAGA/GA

print('percentage: ' + str(percent))
print('SAGA     damage: ' + str(SAGA))
print('GreatAxe damage: ' + str(GA))


SAGS = 0
GS = 0


for j in range(sample):
    roll1 = random.randint(1,6) + random.randint(1,6)
    roll2 = random.randint(1,6) + random.randint(1,6)
    SAGS += max(roll1, roll2)
    GS += random.randint(1,12)

percent = SAGS/GS

print('percentage: ' + str(percent))
print('SAGS       damage: ' + str(SAGS))
print('GreatSword damage: ' + str(GS))
