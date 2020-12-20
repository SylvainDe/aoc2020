# vi: set shiftwidth=4 tabstop=4 expandtab:
import datetime
import math


def get_tiles_from_file(file_path="day20_input.txt"):
    with open(file_path) as f:
        return get_tiles_from_string(f.read())


def get_tile_borders(content):
    # The outside of the tile determines how it's used
    return (
        content[0],
        "".join(line[-1] for line in content),
        content[-1][::-1],
        "".join(line[0] for line in content)[::-1],
    )


def get_rotations_and_symetries(tile):
    a, b, c, d = tile
    a2, b2, c2, d2 = a[::-1], b[::-1], c[::-1], d[::-1]
    return [
        # Rotations
        [a, b, c, d],  # Identity
        [b, c, d, a],  # 90°
        [c, d, a, b],  # 180° - central symetry
        [d, a, b, c],  # 270°
        # Vertical flip
        [a2, d2, c2, b2],
        # Horizontal flip
        [c2, b2, a2, d2],
    ]


def get_tile_from_string(string):
    lines = string.splitlines()
    number = int(lines[0][len("Tiles:") - 1 : -1])
    return number, lines[1:]


def get_tiles_from_string(string):
    tiles_dict = dict()
    for s in string.split("\n\n"):
        nb, cont = get_tile_from_string(s)
        tiles_dict[nb] = cont
    return tiles_dict


def guess_corners(tiles):
    tiles_borders = {k: get_tile_borders(v) for k, v in tiles.items()}
    sides = dict()
    for n, tile in tiles_borders.items():
        for side in tile:
            for s in (side, side[::-1]):
                sides.setdefault(s, []).append(n)
    # (1, 1, X, Y) are corners
    # (1, X, Y, Z) are sides
    corners = []
    for n, tile in tiles_borders.items():
        caracterictics = tuple(sorted(len(sides[side]) for side in tile))
        if caracterictics[0] == caracterictics[1] == 1:
            corners.append(n)
    if len(corners) == 4:
        return corners
    return None


def guess_image(tiles):
    tiles_borders = {k: get_tile_borders(v) for k, v in tiles.items()}
    sides = dict()
    for n, tile in tiles_borders.items():
        for side in tile:
            for s in (side, side[::-1]):
                sides.setdefault(s, []).append(n)

    # Determine corners and sides
    # (1, 1, X, Y) are corners
    # (1, X, Y, Z) are sides
    corners, borders, middles = [], [], []
    for n, tile in tiles_borders.items():
        caracterictics = tuple(sorted(len(sides[side]) for side in tile))
        if caracterictics[0] == 1:
            if caracterictics[1] == 1:
                corners.append(n)
            else:
                borders.append(n)
        else:
            middles.append(n)

    # Check that what we have found makes sense
    nb_tiles = len(tiles)
    side_len = int(math.sqrt(nb_tiles))
    assert side_len * side_len == nb_tiles

    assert len(corners) == 4
    assert len(borders) + len(corners) == 4 * (side_len - 1)

    # Build image starting from a corner
    for a, b, c, d in get_rotations_and_symetries(tiles_borders[corners[0]]):
        if len(sides[a]) == 1 == len(sides[d]):
            print(a, b, c, d)


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
    print(guess_image(tiles))


def get_solutions():
    tiles = get_tiles_from_file()
    print(mult(guess_corners(tiles)) == 140656720229539)
    print(guess_image(tiles))


if __name__ == "__main__":
    begin = datetime.datetime.now()
    run_tests()
    get_solutions()
    end = datetime.datetime.now()
    print(end - begin)
