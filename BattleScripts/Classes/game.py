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

    def __init__(self, hp, mp, atk, df, magic, items, name):
        self.maxHp = hp
        self.hp = hp
        self.maxMp = mp
        self.mp = mp
        self.atkH = atk + 10
        self.atkL = atk - 10
        self.df = df
        self.magic = magic
        self.items = items
        self.action = ["Attack","Magic","Items"]
        self.name = name

    def genDmg(self):
        return random.randrange(self.atkL,self.atkH)

    '''def genSpellDmg(self, i):
        mgL = self.magic[i]["dmg"]-5
        mgH = self.magic[i]["dmg"]+5
        return random.randrange(mgL, mgH)'''

    def takeDmg(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def getHp(self):
        return self.hp

    def getMaxhp(self):
        return self.maxHp

    def getMp(self):
        return self.mp

    def getMaxmp(self):
        return self.maxMp

    def heal(self,dmg):
        self.hp += dmg
        if self.hp > self.maxHp:
            self.hp = self.maxHp
        return self.hp

    def reduceMp(self, cost):
        if self.mp > cost:
            self.mp -= cost
            return True
        else:
            return False

    '''def getSpellName(self, i):
        return self.magic[i]["name"]

    def getSpellCost(self, i):
        return self.magic[i]["cost"]'''

    def chooseAction(self):
        i = 1
        print('\n'+bcolours.BOLD+self.name+bcolours.ENDC)
        print ("Actions")
        for item in self.action:
            print (str(i) + ':', item)
            i += 1

    def chooseMagic(self):
        i = 1
        print ("Magic")
        for spell in self.magic:
            print("\n"+str(i) + ':', spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def chooseItem(self):
        i=1
        print("Items")
        for item in self.items:
            print("\n"+str(i)+":", item["item"].name, ":", item["item"].description, "(x"+str(item["quantity"])+")")
            i+=1

    def getStats(self):
        hpBar = ''
        mpBar = ''
        barTick = (self.hp/self.maxHp)*100/5

        while barTick >0:
            hpBar+='█'
            barTick-=1
        while len(hpBar)<20:
            hpBar+=' '
        barTick = (self.mp/self.maxMp)*100/5
        while barTick >0:
            mpBar+='█'
            barTick-=1
        while len(mpBar)<20:
            mpBar+=' '

        print('                               ____________________               ____________________ ')
        print(bcolours.BOLD+self.name+'          '+
              str(self.hp)+'/'+str(self.maxHp)+'    |'+bcolours.OKGREEN+hpBar+bcolours.ENDC+'|    '+bcolours.BOLD+
              str(self.mp)+'/'+str(self.maxMp)+'    |'+bcolours.OKBLUE+mpBar+bcolours.ENDC+'|')
