inventory = []


class Item(object):
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self. weight = weight

    def name(self):
        print("Jolt")

    def value(self):
        print("The % cost 20-90 coins" % self.value)

    def weight(self):
        print("The % is about 12 pound" % self.weight)

    def pick_up(self):
        print("You pick up the %s" % self.name)


class Weapon(Item):
    def __init__(self, name, value, weight):
        super(Weapon, self).__init__(name, value, weight)

    def fire(self):
        print("You shot the gun.")


class Pistol(Weapon):
    def __int__(self, name, value, weight):
        super(Pistol, self).__init__(name, value, weight)

    def fire(self):
        print("You fire the gun.")


class Shotgun(Weapon):
    def __init__(self, name, value, weight):
        super(Shotgun, self).__init__(name, value, weight)

    def fire(self):
        print("You fire the gun.")


class Knife(Weapon):
    def __init__(self, name, value, weight):
        super(Knife, self).__init__(name, value, weight)


class M16(Weapon):
    def __init__(self, name, value, weight):
        super(M16, self).__init__(name, value, weight)

    def fire(self):
        print("You fire the gun.")


class Ammo(Item):
    def __init__(self, name, value, weight):
        super(Ammo, self).__init__(name, value, weight)


class Size(Ammo):
    def __init__(self, name, value, weight):
        super(Size, self).__init__(name, value, weight)

    def Reload(self):
        print("You reload the gun")


class Attachments(Item):
    def __init__(self, name, value, weight):
        super(Attachments, self).__init__(name, value, weight)


class PistolSilencer(Attachments):
    def __init__(self, name, value, weight):
        super(PistolSilencer, self).__init__(name, value, weight)


class Scope(Attachments):
    def __init__(self, name, value, weight):
        super(Scope, self).__init__(name, value, weight)


class Armor(Item):
    def __init__(self, name, value, weight):
        super(Armor, self).__init__(name, value, weight)


class HeavyArmor(Armor):
    def __init__(self, name, value, weight):
        super(HeavyArmor, self).__init__(name, value, weight)


class LightArmor(Armor):
    def __init__(self, name, value, weight):
        super(LightArmor, self).__init__(name, value, weight)


class HealingItem(Item):
    def __init__(self, name, value, weight):
        super(HealingItem, self).__init__(name, value, weight)


class Bandage(HealingItem):
    def __init__(self, name, value, weight):
        super(Bandage, self).__init__(name, value, weight)


class MedicPack(HealingItem):
    def __init__(self, name, value, weight):
        super(MedicPack, self).__init__(name, value, weight)


weapon_list = [Shotgun, M16, Pistol]


class Characters(object):
    def __init__(self, name, health, attack, take_damage, death, locations=None):
        self.name = name
        self.health = health
        self.attack = attack
        self.take_damage = take_damage
        self.death = death
        self.location = locations
        self.inventory = []

    def move(self, directions):
        try:
            self.location = globals()[getattr(self.location, directions)]
        except KeyError:
            pass


class Hero(Characters):
    def __int__(self, name, health, attack, take_damage, death):
        super(Hero, self).__init__(name, health, attack, take_damage, death)

    def pick_up(self, item):
        self.inventory.append(item)

class Monster(Characters):
    def __init__(self, name ,health, attack, take_damage, death):
        super(Monster, self).__init__(name, health, attack, take_damage, death)

    def attack(self):
        Hero.attack(self.name)


# Rooms
class Room(object):
    def __init__(self, south, east, name, north, west, north_east, north_west, description, enemies, item=[]):
        if item is None:
            item = []
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.northeast = north_east
        self.northwest = north_west
        self.description = description
        self.enemies = enemies
        self.item = item
        self.character = []


    # Weapons

Pistol = Pistol("Pistol", 50, 3)
Shotgun = Shotgun("Shotgun", 70, 6)
Knife = Knife("Knife", 25, 1)
M16 = M16("M16", 60, 7.5)
PistolSilencer = PistolSilencer("PistolSilencer", 100, 1)
Scope = Scope("Scope", 150, 2)
HeavyArmor = HeavyArmor("HeavyArmor", 175, 10)
LightArmor = LightArmor("LightArmor", 125, 6)
Bandage = Bandage("Bandage", 20, 0)
MedicPack = MedicPack("MedicPack", 50, 2)

    # Characters

hero = Hero("Bolt", 100, 20, 15, "You died.")
monster = Monster("Toxic", 400, 4, 10, "You killed the monster")


    # Rooms

S_Gate = Room(None, None, "South Gate", "N_Office", None, None, None, "You are at south entrance.", None)
N_Office = Room(None, "E_GYM", "North Office", None, "W_Library", None, None, "You are "
"at front office.", None, [Bandage])
E_GYM = Room(None, None, "GYM", "N_Tiger_Alley", "W_Office", None, None, "You are now in the gym.", None, [Shotgun])
W_Library = Room("N_Office", None, "Library", "W_Quad", "W_Class_Rooms", None, None, "Your now "
"at the library.", None, [M16])
W_Class_Rooms = Room(None, "W_Library", "Class Rooms", None, None, None, None, "You are at "
"some classrooms.", None, [Scope])
N_Tiger_Alley = Room(None, "W_Quad", "Tiger Alley", None, None, "N_E_BlackTop", None, "You are walking around the "
                                                                                      "alley.", None, [Bandage])
W_Quad = Room("S_Band", "E_ScienceBuilding", "Quad", "N_Tiger_Alley", "W_Library", "N_E_BathRoom", "N_W_Cafeteria",
              "Your now at the quad.", None)
S_Band = Room(None, "S_Band", "Quad", None, None, None, None, "Your now at the band room.", None, [LightArmor])
N_W_Cafeteria = Room(None, "W_Quad", "Cafeteria", None, None, None, None, "You're in the "
"Cafeteria.", None, [PistolSilencer])
N_E_BathRoom = Room(None, None, "BathRoom", None, None, "W_Quad", None, "You are now at the bathroom.", None, [Pistol])
N_E_BlackTop = Room("S_LockerRoom", None, "BlackTop", None, None, "N_Tiger_Alley", None, "You are at the blacktop.",
                    None, [MedicPack])
S_LockerRoom = Room(None, None, "LockerRoom", "N_E_BlackTop", None, None, None, "You are next to a locker room.",
                    None, [HeavyArmor])
E_ScienceBuilding = Room(None, None, "ScienceBuilding", None, "W_WBuilding", None, None, "You are in "
"the science building.", monster, [Knife])
W_WBuilding = Room("W_Quad", None, "WBuilding", None, None, "W_ArtBuilding", None, "You are in the W Building.", None,)
W_ArtBuilding = Room(None, "W_WBuilding", "ArtBuilding", None, None, None, None, "Your now in the the art building.",
                     None,)

def randomize_item_room():
    list_of_items = [Pistol, Shotgun, M16, Knife, MedicPack, Bandage, LightArmor, HeavyArmor, PistolSilencer, Scope]
    list_of_room = [N_Office, E_GYM, W_Library, W_Class_Rooms, N_Tiger_Alley, S_Band, N_W_Cafeteria, N_E_BathRoom,
                    N_E_BlackTop, S_LockerRoom, E_ScienceBuilding]

ghost = [monster]
hero.location = S_Gate
directions = ['north', 'west', 'north', 'east',]
short_directions = ['n', 'w', 'n', 'e',]
randomize_item_room()

def place_ghost():
    for monster in ghost:
        room = E_ScienceBuilding
        monster.location = room


place_ghost()



while True:
    print(hero.location.name)
    print(hero.location.description)

    if E_ScienceBuilding == hero.location:
        print("You got poisoned and died")
        quit(0)

    if len(hero.location.item) > 0:
        print("The following items are here:")
    for item in hero.location.item:
        print(item.name)

    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]

    if command in directions:
        try:
            hero.move(command)
        except KeyError:
            print("You cannot go this way")

    if 'inventory' in command:
        if hero.inventory is not None:
            print(hero.inventory)
        else:
            print('You got nothing in your inventory.')

    elif command == "shoot":
        for item in weapon_list:
            if command == "shoot":
                print("what do you want to shoot with")
            if command == item.name:
                print("you shot with %s" % item.name)

        print("You shot the gun")
    elif 'take' in command:
        item_requested = command[5:]
        remove_item = None
        for item in hero.location.item:
            if item.name.lower() == item_requested.lower():
                hero.pick_up(item)
                print("Taken.")
                remove_item = item
        if remove_item is not None:
            hero.location.item.remove(remove_item)
        else:
            print("I don't see it here.")
    elif hero.health <= 0:
        print("You Died")
        break
    else:
        if command in short_directions:
            try:
                hero.location
            except KeyError:
                print("Command not recognized")
    place_ghost()