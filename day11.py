import itertools


def get_seat_layout_from_file(file_path="day11_input.txt"):
    with open(file_path) as f:
        return {
            (i, j): s for i, line in enumerate(f) for j, s in enumerate(line.strip())
        }


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


def perform_one_seat_change_round_rule1(seats):
    return {pos: get_new_seat_value_rule1(seats, pos) for pos in seats.keys()}


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


def perform_one_seat_change_round_rule2(seats):
    return {pos: get_new_seat_value_rule2(seats, pos) for pos in seats.keys()}


def get_nb_seat_on_fixedpoint(seats, func):
    while True:
        new_seats = func(seats)
        if new_seats == seats:
            break
        seats = new_seats
    return sum(seat == "#" for seat in seats.values())


def run_tests():
    example1_str = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
    example1 = {
        (i, j): s
        for i, line in enumerate(example1_str.split("\n"))
        for j, s in enumerate(line)
    }
    assert (
        get_nb_seat_on_fixedpoint(example1, perform_one_seat_change_round_rule1) == 37
    )
    assert (
        get_nb_seat_on_fixedpoint(example1, perform_one_seat_change_round_rule2) == 26
    )


def get_solutions():
    seat_layout = get_seat_layout_from_file()
    print(
        get_nb_seat_on_fixedpoint(seat_layout, perform_one_seat_change_round_rule1)
        == 2204
    )
    print(
        get_nb_seat_on_fixedpoint(seat_layout, perform_one_seat_change_round_rule2)
        == 1986
    )


if __name__ == "__main__":
    run_tests()
    get_solutions()
