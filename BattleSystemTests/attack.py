import random


class Enemy():
    hp = 200

    def __init__(self, atkL, atkH):
        self.atkL = atkL
        self.atkH = atkH

    def getAtk(self):
        atkPow = random.randrange(self.atkL,self.atkH)
        print(atkPow)

    def getHp(self):
        print('Hp is ', self.hp)

enemy1 = Enemy(40, 49)
enemy1.getAtk()
enemy1.getHp()

enemy2 = Enemy(75, 90)
enemy2.getAtk()
enemy2.getHp()


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
