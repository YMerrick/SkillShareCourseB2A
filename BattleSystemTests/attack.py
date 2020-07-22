import random
from Classes.enemy import Enemy

enemy1 = Enemy(200, 60)
print(enemy1.getHp())



'''
playerhp = 400
enemyatkL = 60
enemyatkH = 100

while playerhp > 0:
    dmg = random.randrange(enemyatkL,enemyatkH)

    playerhp -= dmg

    if playerhp <= 30:
        playerhp = 30

    print('Player is attacked for', dmg,'they now have', playerhp)


    if playerhp >30:
        continue

    print('You have low health. You have been teleported to the nearest checkpoint')
    break '''
