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


class Weapon(Item):
    def __init__(self, name, value, weight):
        super(Weapon,self).__init__(name, value, weight)

    def fire(self):
        print("You shot the gun.")


class Pistol(Weapon):
    def __int__(self, name, value, weight):
        super(Pistol, self).__int__(name, value, weight)


class Shotgun(Weapon):
    def __init__(self, name, value, weight):
        super(Shotgun, self).__init__(name, value, weight)


class knives(Weapon):
    def __init__(self, name, value, weight):
        super(knives, self).__init__(name, value, weight)

class M_16(Weapon):
    def __init__(self, name, value, weight):
        super(M_16, self).__init__(name, value, weight)


class Attachments(Item):
    def __init__(self, name, value, weight):
        super(Attachments, self).__init__(name, value, weight)


class Pistol_Silencer(Attachments):
    def __init__(self, name, value, weight):
        super(Pistol_Silencer, self).__init__(name, value, weight)


class Scope(Attachments):
    def __init__(self, name, value, weight):
        super(Scope, self).__init__(name, value, weight)


class Armor(Item):
    def __init__(self, name, value, weight):
        super(Armor, self).__init__(name, value, weight)


class Heavy_Armor(Armor):
    def __init__(self, name, value, weight):
        super(Heavy_Armor, self).__init__(name, value, weight)


class Light_Armor(Armor):
    def __init__(self, name, value, weight):
        super(Light_Armor, self).__init__(name, value, weight)


class Healing_Item(Item):
    def __init__(self, name, value, weight):
        super(Healing_Item, self).__init__(name, value, weight)


class Bandage(Healing_Item):
    def __init__(self, name, value, weight):
        super(Bandage, self).__init__(name, value, weight)


class Medic_Pack(Healing Item):
    def __init__(self, name, value, weight):
        super(Medic_Pack, self).__init__(name, value, weight)

