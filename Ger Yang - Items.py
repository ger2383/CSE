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
