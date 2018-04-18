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


class Characters(object):
     def __init__(self, name, health, attack, take_damage, death):
        self.name = name
        self.health = health
        self.attack = attack
        self.take_damage = take_damage
        self.death = death


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

# Rooms
class Room(object):
    def __init__(self, south, east, name, north, west, north_east, north_west, description, item):
        self.item = item
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.north_east = north_east
        self.north_west = north_west
        self.description = description

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

hero = Hero("Bolt", 100, 10, 15, "You died.")
monster = Monster("Toxic", 100, 4, 10, "You killed the monster")


    # Rooms

S_Gate = Room(None, None, "South Gate", "Front Office", None, None, None, "You are at south entrance.")
N_Office = Room(None, "GYM", "North Office", None, "Library", None, None, "You are at front office.")
E_GYM = Room(None, None, "GYM", "Tiger Alley", "Front Office", None, None, "You are now at the gym.")
W_Library = Room("Front Office", None, "Library", "Quad", "Rooms", None, None, "Your now at the library.")
W_Class_Rooms = Room(None, "Library", "Rooms", None, None, None, None, "You are at some classrooms.")
N_Tiger_Alley = Room(None, "Quad", "Tiger Alley", None, None, "BlackTops", None, "You are walking around the alley.")
W_Quad = Room("BandRoom", "TigerAlley", "Quad", None, "Library", "BathRoom", "Cafeteria", "Your now at the quad.")
S_Band = Room(None, "Band", "Quad", None, None, None, None, "Your now at the band room.")
N_W_Cafeteria = Room(None, "Quad", "Cafeteria", None, None, None, None, "Your at the Cafeteria.")
N_E_BathRoom = Room(None, None, "BathRoom", None, None, "Quad", None, "You are now at the bathroom.")
N_E_BlackTop = Room("LockerRoom", None, "BlackTop", None, None, "TigerAlley", None, "You are at the blacktop.")
S_LockerRoom = Room(None, None, "LockerRoom", "BlackTop", None, None, None, "You are next to a locker room.")
E_ScienceBuilding = Room(None, None, "ScienceBuilding", None, "W Building", None, None, "You are at science building.")
W_WBuidling = Room("Quad", None, "W Building", None, None, "Art Building", None, "You are at W Building.")
W_ArtBuilding = Room(None, "WBuilding", "ArtBuilding", None, None, None, None, "Your now at the art building.")

current_node = S_Gate
directions = ['north', 'south', 'east', 'west', 'northeast', '']
short_directions = ['n', 's', 'e', 'w']

while True:
    print(current_node.name)
    print(current_node.description)
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
    # elif command == "shoot":
    #     for Weapon in inventory:
    #         if
            


    else:
        print("Command not recognize")
