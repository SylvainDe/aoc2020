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


def rotate(matrix):
    # https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
    return list(zip(*matrix[::-1]))


def get_rotations_and_symetries(tile):
    t = tile
    yield t
    for i in range(3):
        t = rotate(t)
        yield t
    t = t[::-1]
    yield t
    for i in range(3):
        t = rotate(t)
        yield t


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
    unique_sides = set([s for s, lst in sides.items() if len(lst) == 1])
    corners = [
        n
        for n, tile in tiles_borders.items()
        if sum(side in unique_sides for side in tile) == 2
    ]
    assert len(corners) == 4
    return corners


def guess_image(tiles):
    tiles_borders = {k: get_tile_borders(v) for k, v in tiles.items()}
    sides = dict()
    for n, tile in tiles_borders.items():
        for side in tile:
            for s in (side, side[::-1]):
                sides.setdefault(s, []).append(n)

    unique_sides = set([s for s, lst in sides.items() if len(lst) == 1])

    # Determine corners and sides
    corners, borders, middles = [], [], []
    for n, tile in tiles_borders.items():
        nb_unique = sum(side in unique_sides for side in tile)
        if nb_unique == 2:
            corners.append(n)
        elif nb_unique == 1:
            borders.append(n)
        elif nb_unique == 0:
            middles.append(n)
        else:
            assert False

    # Check that what we have found makes sense
    nb_tiles = len(tiles)
    side_len = int(math.sqrt(nb_tiles))
    assert side_len * side_len == nb_tiles

    assert len(corners) == 4
    assert len(borders) + len(corners) == 4 * (side_len - 1)

    # Build image starting from a corner
    first_line = []
    first_line.append(
        find_match_for_border(tiles, [corners[0]], unique_sides, unique_sides)
    )
    left_col = "".join(line[-1] for line in first_line[-1])
    # Continue to build first line
    for i in range(side_len - 2):
        first_line.append(
            find_match_for_border(tiles, borders, [left_col], unique_sides)
        )
        left_col = "".join(line[-1] for line in first_line[-1])
    first_line.append(
        find_match_for_border(tiles, corners, [left_col], unique_sides, unique_sides)
    )

    # Build second line
    second_line = []
    top_line = "".join(first_line[0][-1])
    second_line.append(find_match_for_border(tiles, borders, unique_sides, [top_line]))
    left_col = "".join(line[-1] for line in second_line[-1])
    for i in range(side_len - 2):
        top_line = "".join(first_line[i + 1][-1])
        second_line.append(
            find_match_for_border(tiles, middles, [left_col], [top_line])
        )
        left_col = "".join(line[-1] for line in second_line[-1])
    top_line = "".join(first_line[side_len - 1][-1])
    second_line.append(
        find_match_for_border(tiles, borders, [left_col], [top_line], unique_sides)
    )

    # Build last line
    third_line = []
    top_line = "".join(second_line[0][-1])
    third_line.append(find_match_for_border(tiles, corners, unique_sides, [top_line]))
    left_col = "".join(line[-1] for line in third_line[-1])
    for i in range(side_len - 2):
        top_line = "".join(second_line[i + 1][-1])
        third_line.append(find_match_for_border(tiles, borders, [left_col], [top_line]))
        left_col = "".join(line[-1] for line in third_line[-1])
    top_line = "".join(second_line[side_len - 1][-1])
    third_line.append(
        find_match_for_border(tiles, corners, [left_col], [top_line], unique_sides)
    )


def find_match_for_border(
    tiles, candidates, left_cols, up_lines, right_cols=None, bottom_line=None
):
    for c in candidates:
        for t in get_rotations_and_symetries(tiles[c]):
            up, left = "".join(t[0]), "".join(line[0] for line in t)
            if up in up_lines and left in left_cols:
                # print(c)
                if right_cols is not None:
                    right = "".join(line[-1] for line in t)
                    assert right in right_cols
                return t
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
    print(guess_image(tiles))
    # print(list(get_rotations_and_symetries([[1, 2], [3, 4]])))
    # print(list(get_rotations_and_symetries([[1, 2, 3], [4, 5, 6], [7, 8, 9]])))


def get_solutions():
    tiles = get_tiles_from_file()
    print(mult(guess_corners(tiles)) == 140656720229539)
    # print(guess_image(tiles))


if __name__ == "__main__":
    begin = datetime.datetime.now()
    run_tests()
    get_solutions()
    end = datetime.datetime.now()
    print(end - begin)
