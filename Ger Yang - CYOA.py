import random
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
        print("You pick up the item")

    def put_on(self):
        print("Attachment on")

    def heal(self):
        print("You just healed")


class Weapon(Item):
    def __init__(self, name, value, weight):
        super(Weapon, self).__init__(name, value, weight)

    def fire(self):
        print("You shot the gun.")


class Pistol(Weapon):
    def __int__(self, name, value, weight):
        super(Pistol, self).__int__(name, value, weight)

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

    def stab(self):
        print("You used the knife.")


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

    def put_on(self):
        Item.put_on(self)


class PistolSilencer(Attachments):
    def __init__(self, name, value, weight):
        super(PistolSilencer, self).__init__(name, value, weight)

    def put_on(self):
        Item.put_on(self.name)


class Scope(Attachments):
    def __init__(self, name, value, weight):
        super(Scope, self).__init__(name, value, weight)

    def put_on(self):
        Item.put_on(self.name)


class Armor(Item):
    def __init__(self, name, value, weight):
        super(Armor, self).__init__(name, value, weight)

    def put_on(self):
        Item.put_on(self.name)


class HeavyArmor(Armor):
    def __init__(self, name, value, weight):
        super(HeavyArmor, self).__init__(name, value, weight)

    def put_on(self):
        Item.put_on(self.name)


class LightArmor(Armor):
    def __init__(self, name, value, weight):
        super(LightArmor, self).__init__(name, value, weight)

    def put_on(self):
        Item.put_on(self.name)


class HealingItem(Item):
    def __init__(self, name, value, weight):
        super(HealingItem, self).__init__(name, value, weight)

    def heal(self):
        Item.heal(self)


class Bandage(HealingItem):
    def __init__(self, name, value, weight):
        super(Bandage, self).__init__(name, value, weight)

    def heal(self):
        Item.heal(self)


class MedicPack(HealingItem):
    def __init__(self, name, value, weight):
        super(MedicPack, self).__init__(name, value, weight)

    def heal(self):
        Item.heal(self)

weapon_list = [Shotgun, M16, Pistol]


class Characters(object):
     def __init__(self, name, health, attack, take_damage, death):
        self.name = name
        self.health = health
        self.attack = attack
        self.take_damage = take_damage
        self.death = death

    def move(self, direction):
        self.location.character.romve(self)
        try:
            self.location = globals()[getattr(self.location, direction)]
        except KeyError:
            pass
        self.location.character.append(self)


class Hero(Characters):
    def __int__(self, name, health, attack, take_damage, death):
        super(Hero, self).__init__(name, health, attack, take_damage, death)

    def pick_up(self):
        Item.pick_up(self.name)

class Monster(Characters):
    def __init__(self, name ,health, attack, take_damage, death):
        super(Monster, self).__init__(name, health, attack, take_damage, death)

    def attack(self):
        Hero.attack(self.name)

    def move(self, direction):
        self.location = globals()[getattr(self.location, direction)]

# Rooms
class Room(object):
    def __init__(self, south, east, name, north, west, north_east, north_west, description, item=None):
        if item is None:
            item = []
        self.item = item
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.northeast = north_east
        self.northwest = north_west
        self.description = description
        self.item = item

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]
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

S_Gate = Room(None, None, "South Gate", "N_Office", None, None, None, "You are at south entrance.", [None])
N_Office = Room(None, "E_GYM", "North Office", None, "W_Library", None, None, "You are at front office.", [Bandage])
E_GYM = Room(None, None, "GYM", "N_Tiger_Alley", "W_Office", None, None, "You are now in the gym.", [Shotgun])
W_Library = Room("S_Office", None, "Library", "N_Quad", "W_Class_Rooms", None, None, "Your now at the library.", [M16])
W_Class_Rooms = Room(None, "E_Library", "Class Rooms", None, None, None, None, "You are at some classrooms.", [Scope])
N_Tiger_Alley = Room(None, "E_Quad", "Tiger Alley", None, None, "N_E_BlackTop", None, "You are walking around the "
                                                                                      "alley.",[Bandage])
W_Quad = Room("S_Band", "E_Tiger_Alley", "Quad", None, "W_Library", "N_E_BathRoom", "N_W_Cafeteria", "Your now at the "
                                                                                                     "quad.", [None])
S_Band = Room(None, "E_Band", "Quad", None, None, None, None, "Your now at the band room.", [LightArmor])
N_W_Cafeteria = Room(None, "E_Quad", "Cafeteria", None, None, None, None, "Your in the Cafeteria.", [PistolSilencer])
N_E_BathRoom = Room(None, None, "BathRoom", None, None, "N_E_Quad", None, "You are now at the bathroom.", [Pistol])
N_E_BlackTop = Room("S_LockerRoom", None, "BlackTop", None, None, "N_E_Tiger_Alley", None, "You are at the blacktop.",
                    [MedicPack])
S_LockerRoom = Room(None, None, "LockerRoom", "N_E_BlackTop", None, None, None, "You are next to a locker room.",
                    [HeavyArmor])
E_ScienceBuilding = Room(None, None, "ScienceBuilding", None, "W_WBuilding", None, None, "You are in"
                                                                                    "the science building.", [Knife])
W_WBuilding = Room("Quad", None, "WBuilding", None, None, "N_E_ArtBuilding", None, "You are in the W Building.", [None])
W_ArtBuilding = Room(None, "E_WBuilding", "ArtBuilding", None, None, None, None, "Your now in the the art building.",
                     [None])

def randomize_item_room():
    list_of_items = [Pistol, Shotgun, M16, Knife, MedicPack, Bandage, LightArmor, HeavyArmor, PistolSilencer, Scope]
    list_of_room = [N_Office, E_GYM, W_Library, W_Class_Rooms, N_Tiger_Alley, S_Band, N_W_Cafeteria, N_E_BathRoom,
                    N_E_BlackTop, S_LockerRoom, E_ScienceBuilding]

current_node = S_Gate
directions = ['north', 'south', 'east', 'west', 'northeast', '']
short_directions = ['n', 's', 'e', 'w', 'ne']
randomize_item_room()


while True:
    random_numbers = random.randint(1,3)
    print(current_node.name)
    print(current_node.description)

    if current_node.location.item is not None:
        print("There is %s for you to pick up" % current_node.item)
    else:
        print("There is no item for you to pick up.")

    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]

    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way")
    elif command == "shoot":

        for item in weapon_list:
            if command == "shoot":
                print("what do you want to shoot with")
            if command == item.name:
                print("you shot with %s" % item.name)

        print("You shot the gun")
    if 'take' in command:
        if current_node.item is not None:
            hero.pick_up()
            print()
            current_node.item = None
        # hero.pick_up()
    elif hero.health == 0:
        print("You Died")
        break

    else:
        print("Command not recognize")