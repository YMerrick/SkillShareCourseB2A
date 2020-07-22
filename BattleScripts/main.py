from Classes.game import Person, bcolours


magic = [{"name": "Fire","cost": 10,"dmg": 80},
         {"name": "Thunder","cost": 12,"dmg": 90},
         {"name": "Blizzard","cost": 10,"dmg": 60},]

player = Person(400, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0

print(bcolours.FAIL + bcolours.BOLD + "An enemy attacks!" + bcolours.ENDC)

while running:
    print('=============================')
    player.chooseAction()
    choice = input("Choose action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.genDmg()
        enemy.takeDmg(dmg)
        print ('You attacked for ',dmg, 'points of damage.')
    elif index == 1:
        player.chooseMagic()
        magicChoice = int(input("Choose your spell: "))-1
        magicDmg = player.genSpellDmg(magicChoice)
        spell = player.getSpellName(magicChoice)
        cost = player.getSpellCost(magicChoice)
        if player.reduceMp(cost):
            enemy.takeDmg(magicDmg)
            print(bcolours.OKBLUE + "\n" + spell, "deals", str(magicDmg), "points of damage" + bcolours.ENDC)
        else:
            print(bcolours.FAIL + "\nNot enough MP\n" + bcolours.ENDC)
            continue

    enemyChoice = 1

    enemyDmg = enemy.genDmg()
    player.takeDmg(enemyDmg)
    print('Enemy attacks for', enemyDmg)

    print('=============================')
    print('Enemy HP:', bcolours.FAIL + str(enemy.getHp()) + "/" + str(enemy.getMaxhp()) + bcolours.ENDC)
    print('Player HP:', bcolours.OKGREEN + str(player.getHp()) + "/" + str(player.getMaxhp()) + bcolours.ENDC)
    print('Player MP:', bcolours.OKBLUE + str(player.getMp()) + "/" + str(player.getMaxmp()) + bcolours.ENDC)

    if enemy.getHp() == 0:
        print(bcolours.OKGREEN + 'You win!' + bcolours.ENDC)
        running = False
    elif player.getHp() == 0:
        print(bcolours.FAIL + 'You have been defeated!' + bcolours.ENDC)
        running = False
