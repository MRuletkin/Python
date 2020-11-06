import random
class Unit:
    def __init__(self, name, clan, health=100, power=10, dexterity=10, intelligence=10):
        self.name = name
        self.clan = clan
        self.health = health
        self.power = power
        self.dexterity = dexterity
        self.intelligence = intelligence

    def health_level(self):
        return random.randint(1, 100)

    def p_d_i(self):
        return random.randint(1, 10)

    def health_increase(self):
        if self.health <= 90:
            self.health += 10

    def __repr__(self):
        return f'Unit name: {self.name}, Clan: {self.clan}, Health: {self.health}, Power: {self.power}, Dexterity: {self.dexterity}, Intelligence: {self.intelligence}'

class Mage(Unit):
    def __init__(self, name, clan, type_of_magic = None, health=100, power=10, dexterity=10, intelligence=10):
        super().__init__(name, clan, health, power, dexterity, intelligence)
        if not type_of_magic:
            self.type_of_magic = random.choice(['Water Mage', 'Wind Mage', 'Fire Mage'])
        else:
            self.type_of_magic = type_of_magic

        self.health = self.health_level()
        self.power = self.p_d_i()
        self.dexterity = self.p_d_i()
        self.intelligence = self.p_d_i()

    def __repr__(self):
        return f'Mage name: {self.name}, Clan: {self.clan}, Type of magic: {self.type_of_magic}, Health: {self.health}, Power: {self.power}, Dexterity: {self.dexterity}, Intelligence: {self.intelligence}'

    def intelligence_increase(self):
        if self.intelligence <= 9:
            self.intelligence += 1

class Archer(Unit):
    def __init__(self, name, clan, type_of_bow=None, health=100, power=10, dexterity=10, intelligence=10):
        super().__init__(name, clan, health, power, dexterity, intelligence)
        if not type_of_bow:
            self.type_of_bow = random.choice(['Bow', 'Crossbow'])
        else:
            self.type_of_bow = type_of_bow

        self.health = self.health_level()
        self.power = self.p_d_i()
        self.dexterity = self.p_d_i()
        self.intelligence = self.p_d_i()

    def __repr__(self):
        return f'Archer name: {self.name}, Clan: {self.clan}, Type_of_bow: {self.type_of_bow}, Health: {self.health}, Power: {self.power}, Dexterity: {self.dexterity}, Intelligence: {self.intelligence}'

    def dexterity_increase(self):
        if self.dexterity <= 9:
            self.dexterity += 1

class Knight(Unit):
    def __init__(self, name, clan, weapon=None, health=100, power=10, dexterity=10, intelligence=10):
        super().__init__(name, clan, health, power, dexterity, intelligence)
        if not weapon:
            self.weapon = random.choice(['Sword', 'Axe', 'Pike'])
        else:
            self.weapon = weapon

        self.health = self.health_level()
        self.power = self.p_d_i()
        self.dexterity = self.p_d_i()
        self.intelligence = self.p_d_i()

    def __repr__(self):
        return f'Knight name: {self.name}, Clan: {self.clan}, Weapon: {self.weapon} Health: {self.health}, Power: {self.power}, Dexterity: {self.dexterity}, Intelligence: {self.intelligence}'

    def power_increase(self):
        if self.power <= 9:
            self.power += 1

knight = Knight('Arthur', 'Tirsh', 'Button')
print(knight)
knight.power_increase()
print(knight)
knight.health_increase()
print(knight)
knight.dexterity_increase()
