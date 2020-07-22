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
    pass
