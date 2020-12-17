# vi: set shiftwidth=4 tabstop=4 expandtab:
import itertools
import collections


def get_state_from_string(string):
    return {
        (i, j, 0)
        for i, l in enumerate(string.split("\n"))
        for j, c in enumerate(l)
        if c == "#"
    }


def get_state_from_file(file_path="day17_input.txt"):
    with open(file_path) as f:
        return get_state_from_string(f.read())


def pretty_print_data(data, empty=" "):
    keys = data.keys()
    xmin, ymin, zmin = (min(p[dim] for p in keys) for dim in range(3))
    xmax, ymax, zmax = (max(p[dim] for p in keys) for dim in range(3))
    for z in range(zmin, zmax + 1):
        print("z = %d" % z)
        for x in range(xmin, xmax + 1):
            print("".join(data.get((x, y, z), empty) for y in range(ymin, ymax + 1)))


def pretty_print_state(state):
    data = {p: "#" for p in state}
    pretty_print_data(data, ".")


def pretty_print_neighbours_count(neigh_count):
    data = {p: "{:2d}".format(nb) for p, nb in neigh_count.items()}
    pretty_print_data(data, "  ")


neighbours_coord = [
    c for c in itertools.product((-1, 0, 1), repeat=3) if c != (0, 0, 0)
]


def get_neighbours(p):
    x, y, z = p
    for dx, dy, dz in neighbours_coord:
        yield x + dx, y + dy, z + dz


def get_n_th_state(state, n):
    for i in range(n):
        neigh_count = collections.Counter(p2 for p in state for p2 in get_neighbours(p))
        state = {
            p
            for p, nb_neigh in neigh_count.items()
            if (2 <= nb_neigh <= 3 if p in state else nb_neigh == 3)
        }
    return len(state)


def run_tests():
    example1 = get_state_from_string(
        """.#.
..#
###"""
    )
    print(example1)
    assert get_n_th_state(example1, 6) == 112


def get_solutions():
    state = get_state_from_file()
    print(get_n_th_state(state, 6) == 372)


if __name__ == "__main__":
    run_tests()
    get_solutions()
