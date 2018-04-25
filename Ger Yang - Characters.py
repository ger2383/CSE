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
    def __init__(self, name, health, attack, take_damage, death):
        super(Monster, self).__init__(name, health, attack, take_damage, death)

    def attack(self):
        Hero.attack(self.name)