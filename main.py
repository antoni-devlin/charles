exitcommands = [
    'exit',
    'quit',
    'q',
]

class Player:
    def __init__(self, name, room_name):
        self.name = name
        self.room = world[room_name]

    def move(self, direction):
        if direction not in self.room.exits:
            print("Cannot move in that direction!")
            return
        new_room_name = self.room.exits['room']
        print('Moving to', new_room_name)
        self.room = world[new_room_name]


class Room:
    def __init__(self, name, description, links):
        self.name = name
        self.description = description
        self.links = links

world = {}
world['starting_room'] = Room('starting_room', 'You are in a small bedroom', {'E', 'hallway'})
world['hallway'] = Room('hallway', 'You are in a hallway', {'W', 'starting_room'})








def startingroom():
    print('''
    Charles woke up in a room, not knowing where he was, when he was, or really, WHO he was.
         
    ---------------------------------------------------------------------------------------
    (1) Go to the door, (2) Get back in bed.
    ''')
    selectionlist = ['1', '2']
    choice = selectchoice(selectionlist)

    if choice == '1':
        print("Charles decided to go through the door.")
        hallway()
    else:
        print("Charles decided to get back in bed.")
        backInBed()


def hallway():
    print('''
    Charles went through the door, and into the hallway.

    ---------------------------------------------------------------------------------------
    [No options yet]
    ''')
    selectionlist = ['1', '2']
    choice = selectchoice(selectionlist)


def backInBed():
    print('''
    
    "I'm pretty sure I'm dreaming," said Charles. And with that, he got back in bed, turned his back to the room,
    and faded slowly back into nothingness...
    
    ''')

    ending()

def ending():
    print('''
    
        The End.
        
        
        Play again? (y/n)
    ''')
    replay = input("\n ?")
    if replay.lower() == "n":
        exit(0)
    elif replay.lower() == "y":
        startingRoom()
    else:
        print("Unknown. Please answer y or n.")
        return backInBed()




def selectchoice(selectionlist):
    loop = True
    while loop == True:
        choice = input("\n? ")
        if choice in selectionlist:
            loop = False
            return choice
        elif choice in exitcommands:
            exit(0)
        else:
            print("Unknown Choice")