# vi: set shiftwidth=4 tabstop=4 expandtab:
import itertools
import collections


def get_2d_points_from_string(string):
    return {
        (i, j)
        for i, l in enumerate(string.splitlines())
        for j, c in enumerate(l)
        if c == "#"
    }


def get_2d_points_from_file(file_path="day17_input.txt"):
    with open(file_path) as f:
        return get_2d_points_from_string(f.read())


def map_points_in_n_dim(points, nb_dim):
    return {tuple(list(p) + [0] * (nb_dim - len(p))) for p in points}


def get_neighbours_coord(nb_dim=3):
    origin = tuple([0] * nb_dim)
    return [c for c in itertools.product((-1, 0, 1), repeat=nb_dim) if c != origin]


neighbours_coord_3 = get_neighbours_coord(3)
neighbours_coord_4 = get_neighbours_coord(4)


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
    points = get_2d_points_from_string(example1)
    points_3d = map_points_in_n_dim(points, 3)
    assert get_n_th_state(points_3d, get_neighbours_3, 6) == 112
    points_4d = map_points_in_n_dim(points, 4)
    assert get_n_th_state(points_4d, get_neighbours_4, 6) == 848


def get_solutions():
    points = get_2d_points_from_file()
    points_3d = map_points_in_n_dim(points, 3)
    print(get_n_th_state(points_3d, get_neighbours_3, 6) == 372)
    points_4d = map_points_in_n_dim(points, 4)
    print(get_n_th_state(points_4d, get_neighbours_4, 6) == 1896)


if __name__ == "__main__":
    run_tests()
    get_solutions()
