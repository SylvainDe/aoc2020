# vi: set shiftwidth=4 tabstop=4 expandtab:
import itertools


def string_to_seat_layout(string):
    return {
        (i, j): s
        for i, line in enumerate(string.split("\n"))
        for j, s in enumerate(line)
    }


def seat_layout_to_string(seats):
    m = max(i for i, j in seats.keys())
    n = max(j for i, j in seats.keys())
    return "\n".join("".join(seats[(i, j)] for j in range(n + 1)) for i in range(m + 1))


def get_seat_layout_from_file(file_path="day11_input.txt"):
    with open(file_path) as f:
        return string_to_seat_layout(f.read())


directions = [pos for pos in itertools.product((-1, 0, +1), repeat=2) if pos != (0, 0)]


def get_nb_occupied_neighbours(seats, pos):
    i, j = pos
    positions = [(i + di, j + dj) for (di, dj) in directions]
    return sum(seats.get(pos2, None) == "#" for pos2 in positions)


def get_new_seat_value_rule1(seats, pos):
    seat = seats[pos]
    if seat == "L":
        return "#" if get_nb_occupied_neighbours(seats, pos) == 0 else seat
    elif seat == "#":
        return "L" if get_nb_occupied_neighbours(seats, pos) >= 4 else seat
    return seat


def get_nb_visible_occupied_seats(seats, pos):
    i, j = pos
    nb = 0
    for di, dj in directions:
        for d in itertools.count(start=1):
            pos2 = i + (d * di), j + (d * dj)
            seat = seats.get(pos2, None)
            if seat != ".":
                nb += seat == "#"
                break
    return nb


def get_new_seat_value_rule2(seats, pos):
    seat = seats[pos]
    if seat == "L":
        return "#" if get_nb_visible_occupied_seats(seats, pos) == 0 else seat
    elif seat == "#":
        return "L" if get_nb_visible_occupied_seats(seats, pos) >= 5 else seat
    return seat


def get_new_seats(seats, func):
    return {pos: func(seats, pos) for pos in seats.keys()}


def get_nb_seat_on_fixedpoint(seats, func):
    while True:
        new_seats = get_new_seats(seats, func)
        if new_seats == seats:
            break
        seats = new_seats
    return sum(seat == "#" for seat in seats.values())


def run_tests():
    example1 = string_to_seat_layout(
        """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
    )
    example1_step = get_new_seats(example1, get_new_seat_value_rule1)
    example2 = string_to_seat_layout(
        """#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##"""
    )
    example3a = string_to_seat_layout(
        """#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##"""
    )
    example3b = string_to_seat_layout(
        """#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#"""
    )

    assert example2 == get_new_seats(example1, get_new_seat_value_rule1)
    assert example3a == get_new_seats(example2, get_new_seat_value_rule1)
    assert get_nb_seat_on_fixedpoint(example1, get_new_seat_value_rule1) == 37

    assert example2 == get_new_seats(example1, get_new_seat_value_rule2)
    assert example3b == get_new_seats(example2, get_new_seat_value_rule2)
    assert get_nb_seat_on_fixedpoint(example1, get_new_seat_value_rule2) == 26


def get_solutions():
    seat_layout = get_seat_layout_from_file()
    print(get_nb_seat_on_fixedpoint(seat_layout, get_new_seat_value_rule1) == 2204)
    print(get_nb_seat_on_fixedpoint(seat_layout, get_new_seat_value_rule2) == 1986)


if __name__ == "__main__":
    run_tests()
    get_solutions()
