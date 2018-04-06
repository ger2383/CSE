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
        super(Weapon,self).__init__(name, value, weight)

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


class knive(Weapon):
    def __init__(self, name, value, weight):
        super(knive, self).__init__(name, value, weight)

    def Stab(self):
        print("You used the knive.")


class M_16(Weapon):
    def __init__(self, name, value, weight):
        super(M_16, self).__init__(name, value, weight)

    def fire(self):
        print("You fire the gun.")


class Attachments(Item):
    def __init__(self, name, value, weight):
        super(Attachments, self).__init__(name, value, weight)

    def put_on(self):
        Item.put_on(self)


class Pistol_Silencer(Attachments):
    def __init__(self, name, value, weight):
        super(Pistol_Silencer, self).__init__(name, value, weight)

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


class Heavy_Armor(Armor):
    def __init__(self, name, value, weight):
        super(Heavy_Armor, self).__init__(name, value, weight)

    def put_on(self):
        Item.put_on(self.name)


class Light_Armor(Armor):
    def __init__(self, name, value, weight):
        super(Light_Armor, self).__init__(name, value, weight)

    def put_on(self):
        Item.put_on(self.name)


class Healing_Item(Item):
    def __init__(self, name, value, weight):
        super(Healing_Item, self).__init__(name, value, weight)

    def heal(self):
        Item.heal(self)


class Bandage(Healing_Item):
    def __init__(self, name, value, weight):
        super(Bandage, self).__init__(name, value, weight)

    def heal(self):
        Item.heal(self)

class Medic_Pack(Healing_Item):
    def __init__(self, name, value, weight):
        super(Medic_Pack, self).__init__(name, value, weight)

    def heal(self):
        Item.heal(self)


         # Rooms
class Room(object):
    def __init__(self, south, east, name, north, west, north_east, north_west, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]

S_Gate = Room(None, None, "South Gate", "Front Office", None, "You are at south entrance.")
N_Office = Room(None, "GYM", "North Office", None, "Library", "You are at front office")
E_GYM = Room(None, None, "GYM", "Tiger Alley", "Front Office", "You are now at the gym")
W_Library = Room("Front Office", None, "Library", "Quad", "Rooms", "Your now at the library")
W_Class_Rooms = Room(None,"Library", "Rooms", None, None, "You are at some classrooms")
N_Tiger_Alley = Room(None, "Quad", "Tiger Alley", None, None, "BlackTops", None, None)
W_Quad = Room("BandRoom", "TigerAlley", "Quad", None, "Library", "BathRoom", "Cafeteria", "Your now at the quad.")
S_Band = Room( None, "Band", "Quad", None, None, None, None, "Your now at the band room.")
N_W_Cafeteria = Room(None, "Quad", "Cafeteria", None, None, None, None, "Your at the Cafeteria.")
N_E_BathRoom = Room(None, None, "BathRoom", None, None, "Quad", None, "You are now at the bathroom.")
N_E_BlackTop = Room("LockerRoom", None, "BlackTop", None, None, "TigerAlley", None, "You are at the blacktop.")
S_LockerRoom = Room(None, None, "LockerRoom", "BlackTop", None, None, None, "You are next to a locker room.")
E_ScienceBuilding = Room(None, None, "ScienceBuilding", None, "W Building", None, None, "You are at science building.")
W_WBuidling = Room("Quad", None, "W Building", None, None, "Art Building", None, "You are at W Building")
W_ArtBuilding = Room(None, "WBuilding", "ArtBuilding", None, None, None, None, "Your now at the art building.")

current_node = S_Gate['S. Gate']
directions = ['north', 'south', 'east', 'west', 'northeast', '']
short_directions = ['n', 's', 'e', 'w']

while True:
    print(current_node['Name']) # Change
    print(current_node['Description']) # Change
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:

            # Change
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognize")

