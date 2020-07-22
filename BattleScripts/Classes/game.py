import random

class bcolours:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:

    def __init__(self, hp, mp, atk, df, magic):
        self.maxHp = hp
        self.hp = hp
        self.maxMp = mp
        self.mp = mp
        self.atkH = atk + 10
        self.atkL = atk - 10
        self.def = df
        self.magic = magic
        self.action = ["Attack","Magic"]

    def genDmg(self):
        return random.randrange(self.atkL,self.atkH)

    def
