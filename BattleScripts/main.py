from Classes.game import Person, bcolours
from Classes.magic import Spell
from Classes.inventory import Item
import random






#Creat black magic
fire = Spell("Fire", 10, 100, "Black")
thunder = Spell("Thunder", 10, 100, "Black")
blizzard = Spell("Blizzard", 10, 100, "Black")
meteor = Spell("Meteor", 20, 200, "Black")
quake = Spell("Quake", 14, 140, "Black")

#Create white magic
cure = Spell("Cure", 12, 120, "White")
cura = Spell("Cura", 18, 200, "White")

#Create some Items
potion = Item("Potion", "potion", "Heals 50HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500HP", 500)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 99999)
hielixir = Item("Mega Elixir", "elixir", "Fully restores party's HP/MP", 50)

grenade = Item("Grenade", "attack", "Deals 500HP", 500)

playerSpells = [fire, thunder, blizzard, meteor, cure, cura]
playerItem = [{"item": grenade, "quantity": 2},{"item":superpotion,"quantity":2},
              {"item": potion, "quantity": 15},{"item": elixir,"quantity": 1}]

player1 = Person(500, 65, 60, 34, playerSpells, playerItem,"Steve    ")
player2 = Person(500, 65, 60, 34, playerSpells, playerItem,"Herobrine")
player3 = Person(500, 65, 60, 34, playerSpells, playerItem,"Mercy    ")
players = [player1,player2,player3]
enemy1 = Person(5000, 90, 90, 25, [], [], "Bob    ")
enemy2 = Person(1250, 70, 45, 25, [], [], "Charles")
enemy3 = Person(1250, 70, 45, 25, [], [], "Bundy  ")
enemies = [enemy1   ,enemy2,enemy3]

running = True
i = 0

print(bcolours.FAIL + bcolours.BOLD + "An enemy attacks!" + bcolours.ENDC)

while running:
    print('=============================')

    print('\n\n')
    print('Name                           HP                                 MP')
    for player in players:
        player.getStats()
    print('\n')

    for enemy in enemies:
        enemy.getEnemyStats()
    print('\n\n')

    for player in players:


        player.chooseAction()
        choice = input("Choose action: ")
        index = int(choice) - 1

        if index == 0:
            dmg = player.genDmg()
            enemy.takeDmg(dmg)
            print ('You attacked for ',dmg, 'points of damage.')


        elif index == 1:
            player.chooseMagic()
            magicChoice = int(input("\nChoose your spell: "))-1
            if magicChoice == -1:
                continue

            spell = player.magic[magicChoice]
            magicDmg = spell.genDmg()


            if player.reduceMp(spell.cost):
                if spell.type == "White":
                    player.heal(magicDmg)
                    print(bcolours.OKBLUE + "\n" + spell.name+" heals for", magicDmg, "HP"+bcolours.ENDC)
                elif spell.type == "Black":
                    enemy.takeDmg(magicDmg)
                    print(bcolours.OKBLUE + "\n" + spell.name, "deals", str(magicDmg), "points of damage" + bcolours.ENDC)
            else:
                print(bcolours.FAIL + "\nNot enough MP\n" + bcolours.ENDC)
                continue


        elif index == 2:
            player.chooseItem()
            itemChoice = int(input("\nChoose your item: "))-1

            if itemChoice == -1:
                continue

            item = player.items[itemChoice]["item"]

            if player.items[itemChoice]["quantity"] == 0:
                print (bcolours.FAIL+"\nNone left..."+bcolours.ENDC)
                continue

            player.items[itemChoice]["quantity"] -= 1



            if item.type == "potion":
                player.heal(item.prop)
                print(bcolours.OKGREEN+"\n"+item.name, "heals for", str(item.prop), "HP"+bcolours.ENDC)
            elif item.type == "elixir":
                player.hp = player.maxHp
                player.mp = player.maxMp
                print(bcolours.OKGREEN+"\n"+item.name, "fully restores HP/MP"+bcolours.ENDC)
            elif item.type == "attack":
                enemy.takeDmg(item.prop)
                print(bcolours.FAIL + "\n"+item.name, "deals", str(item.prop), "points of damage"+bcolours.ENDC)



    enemyChoice = 1
    target = random.randrange(0,3)

    enemyDmg = enemy.genDmg()
    players[target].takeDmg(enemyDmg)
    print(bcolours.FAIL +'Enemy attacks for', str(enemyDmg) + bcolours.ENDC)

    if enemy.getHp() == 0:
        print(bcolours.OKGREEN + 'You win!' + bcolours.ENDC)
        running = False
    elif player.getHp() == 0:
        print(bcolours.FAIL + 'You have been defeated!' + bcolours.ENDC)
        running = False
