# vi: set shiftwidth=4 tabstop=4 expandtab:
import itertools
import collections


def get_state_from_string(string, nb_dim=3):
    return {
        tuple([i, j] + [0] * (nb_dim - 2))
        for i, l in enumerate(string.split("\n"))
        for j, c in enumerate(l)
        if c == "#"
    }


def get_state_from_file(nb_dim=3, file_path="day17_input.txt"):
    with open(file_path) as f:
        return get_state_from_string(f.read(), nb_dim)


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


neighbours_coord_3 = [
    c for c in itertools.product((-1, 0, 1), repeat=3) if c != (0, 0, 0)
]

neighbours_coord_4 = [
    c for c in itertools.product((-1, 0, 1), repeat=4) if c != (0, 0, 0, 0)
]


def get_neighbours_3(p):
    x, y, z = p
    for dx, dy, dz in neighbours_coord_3:
        yield x + dx, y + dy, z + dz


def get_neighbours_4(p):
    w, x, y, z = p
    for dw, dx, dy, dz in neighbours_coord_4:
        yield w + dw, x + dx, y + dy, z + dz


def get_n_th_state(state, get_neighbours_func, n):
    for i in range(n):
        neigh_count = collections.Counter(
            p2 for p in state for p2 in get_neighbours_func(p)
        )
        state = {
            p
            for p, nb_neigh in neigh_count.items()
            if (2 <= nb_neigh <= 3 if p in state else nb_neigh == 3)
        }
    return len(state)


def run_tests():
    example1 = """.#.
..#
###"""
    state = get_state_from_string(example1, 3)
    assert get_n_th_state(state, get_neighbours_3, 6) == 112
    state = get_state_from_string(example1, 4)
    assert get_n_th_state(state, get_neighbours_4, 6) == 848


def get_solutions():
    state = get_state_from_file()
    print(get_n_th_state(state, get_neighbours_3, 6) == 372)
    state = get_state_from_file(nb_dim=4)
    print(get_n_th_state(state, get_neighbours_4, 6) == 1896)


if __name__ == "__main__":
    run_tests()
    get_solutions()
