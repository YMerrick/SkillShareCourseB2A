class Enemy:

    def __init__(self, hp, mp, atkL = 60, atkH = 100):
        self.maxHp = hp
        self.hp = hp
        self.maxMp = mp
        self.mp = mp
        self.atkL = atkL
        self.atkH = atkH

    def getAtk(self):
        atkPow = random.randrange(self.atkL,self.atkH)
        return atkPow

    def getHp(self):
        return self.hp
