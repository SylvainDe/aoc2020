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
    Direction.EAST: (1, 0),
    Direction.SOUTH: (0, -1),
    Direction.WEST: (-1, 0),
    Direction.NORTH: (0, 1),
}


def state_after_instruction(state, instruction):
    x, y, direc = state
    action, n = instruction[0], int(instruction[1:])
    if action == "N":
        dx, dy = shifting[Direction.NORTH]
        x, y = x + n * dx, y + n * dy
    elif action == "S":
        dx, dy = shifting[Direction.SOUTH]
        x, y = x + n * dx, y + n * dy
    elif action == "E":
        dx, dy = shifting[Direction.EAST]
        x, y = x + n * dx, y + n * dy
    elif action == "W":
        dx, dy = shifting[Direction.WEST]
        x, y = x + n * dx, y + n * dy
    elif action in ("L", "R"):
        rot = (-1 if action == "L" else 1) * n / 90
        direc = Direction((direc.value + rot) % 4)
    elif action == "F":
        dx, dy = shifting[direc]
        x, y = x + n * dx, y + n * dy
    else:
        1 / 0
    return x, y, direc


def state_after_instructions(instructions):
    state = (0, 0, Direction.EAST)
    for ins in instructions:
        state = state_after_instruction(state, ins)
    return state


def state_after_instruction2(state, instruction):
    xs, ys, xw, yw = state
    action, n = instruction[0], int(instruction[1:])
    if action == "N":
        dx, dy = shifting[Direction.NORTH]
        xw, yw = xw + n * dx, yw + n * dy
    elif action == "S":
        dx, dy = shifting[Direction.SOUTH]
        xw, yw = xw + n * dx, yw + n * dy
    elif action == "E":
        dx, dy = shifting[Direction.EAST]
        xw, yw = xw + n * dx, yw + n * dy
    elif action == "W":
        dx, dy = shifting[Direction.WEST]
        xw, yw = xw + n * dx, yw + n * dy
    elif action == "F":
        xs, ys = xs + n * xw, ys + n * yw
    elif action in ("L", "R"):
        rot = ((-1 if action == "L" else 1) * n // 90) % 4
        for i in range(rot):
            xw, yw = yw, -xw
    else:
        1 / 0
    return xs, ys, xw, yw


def state_after_instructions2(instructions):
    state = (0, 0, 10, 1)
    for ins in instructions:
        state = state_after_instruction2(state, ins)
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
    x, y, xw, yw = state_after_instructions2(example1)
    assert abs(x) + abs(y) == 286


def get_solutions():
    instructions = get_instructions_from_file()
    x, y, direct = state_after_instructions(instructions)
    print(abs(x) + abs(y) == 381)
    x, y, xw, yw = state_after_instructions2(instructions)
    print(abs(x) + abs(y) == 28591)


if __name__ == "__main__":
    run_tests()
    get_solutions()
