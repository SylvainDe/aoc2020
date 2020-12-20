# vi: set shiftwidth=4 tabstop=4 expandtab:
import datetime


def get_tiles_from_file(file_path="day20_input.txt"):
    with open(file_path) as f:
        return get_tiles_from_string(f.read())


def get_tile_content_signature(content):
    # The outside of the tile determines how it's used
    return (
        content[0],
        "".join(line[-1] for line in content),
        content[-1],
        "".join(line[0] for line in content),
    )


def get_tile_from_string(string):
    lines = string.splitlines()
    number = int(lines[0][len("Tiles:") - 1 : -1])
    content = get_tile_content_signature(lines[1:])
    return number, content


def get_tiles_from_string(string):
    tiles_dict = dict()
    for s in string.split("\n\n"):
        nb, cont = get_tile_from_string(s)
        tiles_dict[nb] = cont
    return tiles_dict


def guess_corners(tiles):
    sides = dict()
    for n, tile in tiles.items():
        for side in tile:
            s = min(side, side[::-1])
            sides.setdefault(s, []).append(n)
    # (1, 1, X, Y) are corners
    # (1, X, Y, Z) are sides
    corners = []
    for n, tile in tiles.items():
        caracterictics = []
        for side in tile:
            s = min(side, side[::-1])
            caracterictics.append(len(sides[s]))
        caracterictics = tuple(sorted(caracterictics))
        if caracterictics[0] == caracterictics[1] == 1:
            corners.append(n)
    if len(corners) == 4:
        return corners
    return None


def mult(iterator):
    m = 1
    for i in iterator:
        m *= i
    return m


def run_tests():
    example1 = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###..."""
    tiles = get_tiles_from_string(example1)
    assert mult(guess_corners(tiles)) == 20899048083289


def get_solutions():
    tiles = get_tiles_from_file()
    print(mult(guess_corners(tiles)) == 140656720229539)


if __name__ == "__main__":
    begin = datetime.datetime.now()
    run_tests()
    get_solutions()
    end = datetime.datetime.now()
    print(end - begin)
