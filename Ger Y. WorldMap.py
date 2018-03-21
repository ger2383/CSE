class Room(object):
    def __init__(self, south, east, name, north, west, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]

S_Gate = Room(None, None, "South Gate", "Front Office", None, "You are at south entrance.")
N_Office = Room(None, "GYM", "North Office", None, "Library", "You are at front office")
E_GYM = Room(None, None, "GYM", "Tiger Alley", "Front Office", "You are now at the gym")
W_Library = Room("Front Office", None, "Library", "Quad", "Rooms", "Your now at the library")
W_Class_Rooms = Room(None,"Library", "Rooms", None, None, "You are at some classrooms")
N_Tiger_Alley = Room(None, "Quad", "Tiger Alley", )

current_node = S_Gate['S. Gate']
directions = ['north', 'south', 'east', 'west', 'northeast', '']
short_directions = ['n', 's', 'e', 'w']

while True:
    print(current_node['Name']) # Change
    print(current_node['Description']) # Change
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            # Change
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognize")
