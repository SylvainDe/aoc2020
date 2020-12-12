
from enum import Enum

def get_instructions_from_file(file_path="day12_input.txt"):
    with open(file_path) as f:
        return [l.strip() for l in f]



#      y ^ NORTH
#        |
# WEST   |       EAST
# -------+-----> x
#        |
#        |
#        | SOUTH

class Direction(Enum):
    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3

shifting = {
    Direction.EAST:  (1, 0),
    Direction.SOUTH: (0, -1),
    Direction.WEST:  (-1, 0),
    Direction.NORTH: (0, 1),
}




def state_after_instruction(state, instruction):
    x, y, direc = state
    action, n = instruction[0], int(instruction[1:])
    if action == 'N':
        dx, dy = shifting[Direction.NORTH]
        x, y = x+n*dx, y+n*dy
    elif action == 'S':
        dx, dy = shifting[Direction.SOUTH]
        x, y = x+n*dx, y+n*dy
    elif action == 'E':
        dx, dy = shifting[Direction.EAST]
        x, y = x+n*dx, y+n*dy
    elif action == 'W':
        dx, dy = shifting[Direction.WEST]
        x, y = x+n*dx, y+n*dy
    elif action == 'L':
        direc = Direction((direc.value - n/90) % 4)
    elif action == 'R':
        direc = Direction((direc.value + n/90) % 4)
    elif action == 'F':
        dx, dy = shifting[direc]
        x, y = x+n*dx, y+n*dy
    else:
        1/0
    return x, y, direc 


def state_after_instructions(instructions):
    state = (0, 0, Direction.EAST)
    for ins in instructions:
        state = state_after_instruction(state, ins)
    return state

def run_tests():
    example1 = [
"F10",
"N3",
"F7",
"R90",
"F11",
]
    x, y, direct = state_after_instructions(example1)
    assert abs(x) + abs(y) == 25

def get_solutions():
    instructions = get_instructions_from_file()
    x, y, direct = state_after_instructions(instructions)
    print(abs(x) + abs(y) == 381)


if __name__ == "__main__":
    run_tests()
    get_solutions()
