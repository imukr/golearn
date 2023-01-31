from datetime import datetime
from random import randint
import json


''' 
Size of map for moving character
'''
size_n = 10
size_m = 10

'''
Loging all actions with binding timedate
'''

def log(action):
    current_time = datetime.strftime(datetime.now(), '%M:%H')
    message = f'[{current_time}]{action}'
    print(message)

    with open('logs.txt', 'a') as f:
        f.write(f'{message}/n')

'''
Generating map with size size_n, size_m
'''

def generate_map(n, m):
    log('Generating map')
    game_map = []
    for _ in range(n):
        row = [' ' for _ in range(m)]
        game_map.append(row)
    return game_map # First return of game_map


'''
The function that printing game_map
'''

def print_map(game_map):
    log('Printing map')
    for row in game_map:
        print(f"|{'|'.join(row)}|")

'''
The function that adding character, items, obstacls
'''

def generate_world(game_map):
    log('Generating world')
    objs = {'X': 1, 'O': 3, '&': 3, '_': 2}
    size_n, size_m = len(game_map), len(game_map[0])
    rnd_cells = []

    for obj, num in objs.items():
        for i in range(num):
            rnd_cell = randint(0, size_n - 1), randint(0, size_m - 1)
            if rnd_cell not in rnd_cells:
                rnd_cells.append(rnd_cell)
            if rnd_cell in rnd_cells:
                rnd_cell = randint(0, size_n - 1), randint(0, size_m - 1)
                rnd_cells.append(rnd_cell)
            if obj == 'X':
                char_position = list(rnd_cell)

            game_map[rnd_cell[0]][rnd_cell[1]] = obj

    return game_map, char_position # return new game map with character position

def move(dirrection, game_world, char_position):
    game_world[char_position[0]][char_position[1]] = ' '
    print (char_position)

    if dirrection == 'up':
        char_position[0] -= 1
    elif dirrection == 'down':
        char_position[0] += 1
    elif dirrection == 'left':
        char_position[1] -= 1
    elif dirrection == 'right':
        char_position[1] += 1

    game_world[char_position[0]][char_position[1]] = 'X'

    log(f'New position {char_position}')

    return game_world, char_position #return new position character on game_world

def save(game_world, char_position):
    log('Saving game')
    data = {'game_world': game_world, 'char_position': char_position}
    with open('save.txt', 'w') as file:
        json.dump(data, file)
    log('Game saved')


def load():
    log('Loading game')
    with open('save.txt') as file:
        data = json.load(file)
        game_world = data['game_world']
        char = data['char_position']
    return game_world, char
    log('Game loaded')

game_map = generate_map(size_n, size_m)
game_world, char = generate_world(game_map)
print_map(game_world)


''' 
Loop for all games, actions, movings
'''

while True:

    action = input('Chose action: ')

    if action not in ('save', 'move', 'load'):
        log('Wrong action. Try again.')
        continue
    if action == 'save':
        save(game_world, char)
        continue
    if action == 'load':
        game_world, char = load()
        print_map(game_world)
        continue

    dirrection = input('Chose direction: ')

    if dirrection not in ('up', 'down', 'left', 'right'):
        log('Wrong direction. Try again.')
        continue

    game_world, char = move(dirrection, game_world, char)
    print_map(game_world)

