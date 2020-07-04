class Player:
    def __init__(self, name, age, status):
        self.name = name
        self.age = age
        self.status = status

class Object:
    def __init__(self, name, description):
        name = name
        description = description

    def __str__(self):
        return "Name: " + self.name + "\n" \
            + "Description: " + self.description + "\n"

class Weapon(Object):
    def __init__(self, damage):
        damage = damage
