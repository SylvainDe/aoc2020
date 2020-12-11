def get_seat_layout_from_file(file_path="day11_input.txt"):
    with open(file_path) as f:
        return [list(l.strip()) for l in f]

def get_nb_occupied_neighbours(seats, i, j):
    nb = 0
    positions = [(i+di, j+dj) for dj in (-1, 0, +1) for di in (-1, 0, +1) if (di, dj) != (0, 0)]
    for i2, j2 in positions:
        nb += 0 <= i2 < len(seats) and 0 <= j2 < len(seats[i2]) and seats[i2][j2] == "#"
    return nb

def get_new_seat_value(seats, i, j):
    seat = seats[i][j]
    if seat == "L":
        return "#" if get_nb_occupied_neighbours(seats, i, j) == 0 else seat
    elif seat == "#":
        return "L" if get_nb_occupied_neighbours(seats, i, j) >= 4 else seat
    return seat

def perform_one_seat_change_round(seats):
    return [[get_new_seat_value(seats, i, j) for j in range(len(seats[0]))] for i in range(len(seats))]

def perform_seat_change(seats):
    while True:
        new_seats = perform_one_seat_change_round(seats)
        if new_seats == seats:
            break
        seats = new_seats
    return sum(seat == '#' for line in seats for seat in line)

def run_tests():
    example1 = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
    example1_as_list = [list(s) for s in example1.split("\n")]
    # print(example1_as_list)
    # print(perform_one_seat_change_round(example1_as_list))
    assert perform_seat_change(example1_as_list) == 37


def get_solutions():
    seat_layout = get_seat_layout_from_file()
    print(perform_seat_change(seat_layout) == 2204)


if __name__ == "__main__":
    run_tests()
    get_solutions()
