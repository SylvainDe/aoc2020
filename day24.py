# vi: set shiftwidth=4 tabstop=4 expandtab:
import datetime
import collections


def get_directions_from_file(file_path="day24_input.txt"):
    with open(file_path) as f:
        return [l.strip() for l in f]


def sum_elementwise(it1, it2):
    return [sum(x) for x in zip(it1, it2)]


# https://www.redblobgames.com/grids/hexagons/#coordinates
DIRECTIONS = {
    "e": (1, 0),
    "w": (-1, 0),
    "se": (1, 1),
    "sw": (0, 1),
    "ne": (0, -1),
    "nw": (-1, -1),
}


assert DIRECTIONS["nw"] == tuple(sum_elementwise(DIRECTIONS["ne"], DIRECTIONS["w"]))
assert DIRECTIONS["ne"] == tuple(sum_elementwise(DIRECTIONS["nw"], DIRECTIONS["e"]))
assert DIRECTIONS["sw"] == tuple(sum_elementwise(DIRECTIONS["se"], DIRECTIONS["w"]))
assert DIRECTIONS["se"] == tuple(sum_elementwise(DIRECTIONS["sw"], DIRECTIONS["e"]))


def get_tile_from_direction_string(s):
    dirs = list()
    prev = ""
    for c in s:
        pair = prev + c
        direct = DIRECTIONS.get(pair, None)
        if direct is not None:
            dirs.append(direct)
            prev = ""
        else:
            prev = c
    assert prev == ""
    return tuple(sum(x) for x in zip(*dirs))


def get_nb_tiles_flipped(strings):
    c = collections.Counter(get_tile_from_direction_string(s) for s in strings)
    return sum(count % 2 for count in c.values())


def run_tests():
    get_tile_from_direction_string("esew") == (1, 1)
    get_tile_from_direction_string("nwwswee") == (0, 0)
    example1 = [
        "sesenwnenenewseeswwswswwnenewsewsw",
        "neeenesenwnwwswnenewnwwsewnenwseswesw",
        "seswneswswsenwwnwse",
        "nwnwneseeswswnenewneswwnewseswneseene",
        "swweswneswnenwsewnwneneseenw",
        "eesenwseswswnenwswnwnwsewwnwsene",
        "sewnenenenesenwsewnenwwwse",
        "wenwwweseeeweswwwnwwe",
        "wsweesenenewnwwnwsenewsenwwsesesenwne",
        "neeswseenwwswnwswswnw",
        "nenwswwsewswnenenewsenwsenwnesesenew",
        "enewnwewneswsewnwswenweswnenwsenwsw",
        "sweneswneswneneenwnewenewwneswswnese",
        "swwesenesewenwneswnwwneseswwne",
        "enesenwswwswneneswsenwnewswseenwsese",
        "wnwnesenesenenwwnenwsewesewsesesew",
        "nenewswnwewswnenesenwnesewesw",
        "eneswnwswnwsenenwnwnwwseeswneewsenese",
        "neswnwewnwnwseenwseesewsenwsweewe",
        "wseweeenwnesenwwwswnew",
    ]
    assert get_nb_tiles_flipped(example1) == 10


def get_solutions():
    directions = get_directions_from_file()
    print(get_nb_tiles_flipped(directions) == 282)


if __name__ == "__main__":
    begin = datetime.datetime.now()
    run_tests()
    get_solutions()
    end = datetime.datetime.now()
    print(end - begin)
