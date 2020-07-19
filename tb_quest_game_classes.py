#
# define Player class
#
class Player:
    def __init__(self):
        pass
    def __init__(self, name, age, rank):
        self.name = name
        self.age = age
        self.rank = rank

#
# define the Location class
#
class Location:
    def __init__(self, name, description, xp_modifier, health_modifier):
        self.name = name
        self.description = description
        self.xp_modifier = xp_modifier
        self.health_modifier = health_modifier

#
# define Game_Object class and subclasses
#
class Game_Object:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "Name: " + self.name + "\n" \
            + "Description: " + self.description + "\n"

class Weapon(Game_Object):
    def __init__(self, damage):
        damage = damage

class Potion(Game_Object):
    def __init__(self, health):
        health = health

#
# define Npc class and subclasses
#
class Npc:
    def __init__(self, name):
        self.name = name


