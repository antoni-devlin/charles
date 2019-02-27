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


player = Player()
print("Player name: "+ player.name)
print(" ")

aragog = Monster("Aragog", "Giant Spider", 150, "Neutral")

billy = Monster("Billy", "Zombie", 100, "Good")

choice = input('''

What would you like to do?

1) Attack the zombie.
2) Attack the giant spider?

''')


running = True

def main():
    while True:
        if choice == "1":
            print("You swing at " + aragog.name + ", a " + aragog.race + ". He's " + aragog.alignment + "!")
            damage = random.sample(range(1, 40), 1)
            print(damage[0])
            aragog.health += -damage[0]
            print(aragog.health)
            break
        elif choice == "2":
            pass
        else:
            print('''You missed, and now you're dead!
            
            
            Quitting...
            
            ''')
            sys.exit()

main()
