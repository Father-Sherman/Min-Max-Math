import random

sample = int(1000000)

damageGA = 0
damageGS = 0


# for j in range(sample):
#     attackRoll = random.randint(1, 20)
#     if attackRoll == 20:
#         damageGA += (random.randint(1,12) + random.randint(1,12))
#         damageGS += (random.randint(1,6) + random.randint(1,6) + random.randint(1,6))
#     else:
#         damageGA += (random.randint(1,12))
#         damageGS += (random.randint(1,6) + (random.randint(1,6)))

# with constannt advantage
for j in range(sample):
    roll1 = random.randint(1, 20)
    roll2 = random.randint(1, 20)
    attackRoll = max(roll1, roll2)
    if attackRoll == 20:
        damageGA += (random.randint(1,12) + random.randint(1,12))
        damageGS += (random.randint(1,6) + random.randint(1,6) + random.randint(1,6))
    else:
        damageGA += (random.randint(1,12))
        damageGS += (random.randint(1,6) + (random.randint(1,6)))

# when a half orc is weilding weapons they have an additional damage die on crits
# for j in range(sample):
#     attackRoll = random.randint(1, 20)
#     if attackRoll == 20:
#         damageGA += (random.randint(1,12) + random.randint(1,12) + random.randint(1,12))
#         damageGS += (random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + random.randint(1,6))
#     else:
#         damageGA += (random.randint(1,12))
#         damageGS += (random.randint(1,6) + (random.randint(1,6)))

# half orc with constant advantage
# for j in range(sample):
#     roll1 = random.randint(1, 20)
#     roll2 = random.randint(1, 20)
#     attackRoll = max(roll1, roll2)
#     if attackRoll == 20:
#         damageGA += (random.randint(1,12) + random.randint(1,12) + random.randint(1,12))
#         damageGS += (random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + random.randint(1,6))
#     else:
#         damageGA += (random.randint(1,12))
#         damageGS += (random.randint(1,6) + (random.randint(1,6)))

percent = damageGA/damageGS

print('percentage: ' + str(percent))
print('GreatAxe damage: ' + str(damageGA))
print('GreatSword damage: ' + str(damageGS))
