world_map = {
    'S. Gate': {
        'NAME': 'Gate',
        'Description': 'Your at east of entrance gate',
        'PATHS': {
            'NORTH': 'N. Office'
        }
    },
    'N. Office': {
        'NAME': 'Front Office',
        'Description': 'You are at east of office',
        'PATHS': {
            'EAST': 'E. GYM',
            'WEST': 'W. LIBRARY'
        }
    },
    'E. GYM': {
        'NAME': 'GYM',
        'Description': 'Your now at the gym',
        'PATHS': {
            'NORTH': 'N. TIGER ALLEY',
            'WEST': 'W. FRONT OFFICE'
        }
    },
    'W. LIBRARY': {
        'NAME': 'LIBRARY',
        'Description': 'You are now at a Library',
        'PATHS': {
            'WEST': 'W. ROOMS',
            'NORTH': 'N.QUAD',
            'SOUTH': 'S. FRONT OFFICE'
        }
    },
    'W. CLASS ROOMS': {
        'NAME': 'ROOMS',
        'Descriptions': 'Your near some class rooms',
        'PATHS': {
            'EAST': 'E. LIBRARY'
        }
    },
    'N. TIGER ALLEY': {
        'NAME': 'ALLEY',
        'Description': 'Your walking on the alley',
        'PATHS': {
            'EAST': 'E. QUAD',
            'NORTH EAST': 'N.E BLACK TOPS'
        }
    },
    'W. QUAD': {
        'NAME': 'THE QUAD',
        'Description': 'You are now at the quad',
        'PATHS': {
            'EAST': 'E. TIGER ALLEY',
            'NORTH WEST': 'N.W CAFETERIA',
            'NORTH EAST': 'N.E BATHROOMS',
            'SOUTH': 'S. BAND ROOM',
            'WEST': 'W. LIBRARY'
        }
    },
    'S. BAND': {
        'NAME': 'BAND ROOM',
        'Description': 'Your near the band room.',
        'PATHS': {
            'NORTH': 'N. THE QUAD'
        }
    },
    'N.W CAFETERIA': {
        'NAME': 'CAFETERIA',
        'Description': 'Your in the cafeteria',
        'PATHS': {
            'EAST': 'E.THE QUAD'
        }
    },
    'N.E Bathroom': {
        'NAME': 'BATHROOM',
        'Description': 'You finally found the restroom, go pee',
        'PATHS': {
            'North East': 'N.E THE QUAD'
        }
    },
    'N.E Black_Top': {
        'NAME': 'BLACK_TOP',
        'Description': 'You are at the black top',
        'PATHS': {
            'North East': 'N.E TIGERALLEY',
            'South': 'S. LOCKER_ROOMS'
        }
    },
    'S. Locker_Rooms': {
        'NAME': 'LOCKER_ROOMS',
        'Description': 'Your at the locker rooms',
        'PATHS': {
            'North': 'N. BLACK_TOP'
        }
    },
    'E. Science_Building': {
        'NAME': 'SCIENCE_BUILDING',
        'Description': 'Your at the science building',
        'PATHS': {
            'WEST': 'W. W_BUILDING'
        }
    },
    'W. W_BUILDING': {
        'NAME': 'W_BUILDING',
        'Description': 'Your at the wW building',
        'PATHS': {
            'S. THE QUAD',
            'W. ART BUILDING'
        }
    },
    'W. ART BUILDING':{
        'NAME': 'ART BUILDING',
        'Description': 'You are at the art building',
        'PATHS': {
            'E. W_BUILDING'
        }
    }
}

current_node = world_map['S. Gate']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']

while True:
    print(current_node['NAME'])
    print(current_node['Description'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognize")
