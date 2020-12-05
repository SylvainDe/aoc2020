def get_seat_ids_from_file(file_path="day5_input.txt"):
    with open(file_path) as f:
        return set([get_seat_id_from_boarding_pass(l.strip()) for l in f])


def get_seat_id_from_boarding_pass(bp):
    trans_table = str.maketrans("FBLR", "0101")
    binary_bp = bp.translate(trans_table)
    row, col = int(binary_bp[:7], 2), int(binary_bp[7:], 2)
    return row * 8 + col


def run_tests():
    assert get_seat_id_from_boarding_pass("FBFBBFFRLR") == 357
    assert get_seat_id_from_boarding_pass("BFFFBBFRRR") == 567
    assert get_seat_id_from_boarding_pass("FFFBBBFRRR") == 119
    assert get_seat_id_from_boarding_pass("BBFFBBFRLL") == 820


def get_solutions():
    seat_ids = get_seat_ids_from_file()
    max_seat_id = max(seat_ids)
    print(max_seat_id == 850)
    found = None
    for i in range(max_seat_id):
        if (i + 1) in seat_ids and (i - 1) in seat_ids and i not in seat_ids:
            found = i
            break
    print(found == 599)


if __name__ == "__main__":
    run_tests()
    get_solutions()
