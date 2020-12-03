def get_area(file_path='day3_input.txt'):
    with open(file_path) as f:
        return [l.strip() for l in f]

def get_number_of_trees(area):
    x = 0
    dx = 3
    path = []
    for line in area:
        path.append(line[x])
        x = (x + dx) % len(line)
    return sum(x == '#' for x in path)

# Examples provided
area = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]
assert get_number_of_trees(area) == 7

# Real problem
area = get_area()
print(get_number_of_trees(area) == 178)
