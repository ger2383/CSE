class Characters(object):
    def __init__(self, name, health, attack, take_damage, death):
        self.name = name
        self.health = health
        self.attack = attack
        self.take_damage = take_damage
        self.death = death

    def health(self):
