import sys, random


class Player:

    def __init__(self):
        self.name = "Charlie"


class Npc:

    def __init__(self, name):
        self.name = name


class Monster(Npc):

    def __init__(self, name, race, health, alignment):
        super().__init__(name)
        self.race = race
        self.health = int(health)
        self.alignment = alignment
        self.isalive = True


aragog = Monster("Aragog", "Giant Spider", 150, "Neutral")

billy = Monster("Billy", "Zombie", 100, "Good")

enemies = [aragog, billy]

print("You encounter two enemies.")
print("")
for enemy in enemies:
    print("{name}, a {race} with {health} health.".format(name=enemy.name, race=enemy.race, health=enemy.health))
print("")

choice = input("Who would you like to attack? ")

choice = choice.lower()



if choice == aragog.name.lower():
    print("")
    print("Spider!")
    EnemyHealth = aragog.health
    print(EnemyHealth)

elif choice == billy.name.lower():
    print("")
    print("Zombie!")
else:
    print("")
    print("Unknown!")