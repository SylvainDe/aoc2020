# vi: set shiftwidth=4 tabstop=4 expandtab:
import datetime


def get_cups_from_file(file_path="day23_input.txt"):
    with open(file_path) as f:
        for l in f:
            return [int(c) for c in l.strip()]

def perform_move(cups):
    nb_removed = 3
    curr = cups[0]
    removed, remain = cups[1:nb_removed+1], [curr] + cups[nb_removed+1:]
    smaller_cup = [(c, pos) for pos, c in enumerate(remain) if c < curr]
    if smaller_cup:
        dest, dest_pos = max(smaller_cup)
    else:
        dest, dest_pos = max((c, pos) for pos, c in enumerate(remain))
    lst = remain[:dest_pos+1] + removed  + remain[1+dest_pos:]
    curr_idx = lst.index(curr)
    ret = lst[curr_idx+1:] + lst[:curr_idx+1]
    return ret

def perform_moves(cups, nb):
    for i in range(nb):
        cups = perform_move(cups)
    idx = cups.index(1)
    labels = cups[idx+1:] + cups[:idx]
    return int("".join(str(c) for c in labels))

def run_tests():
    example1 = "389125467"
    cups = [int(c) for c in example1]
    # print(cups == [3, 8, 9, 1, 2, 5, 4, 6, 7])
    # cups = perform_move(cups)
    # print(cups == [2, 8, 9, 1, 5, 4, 6, 7, 3])
    # cups = perform_move(cups)
    # print(cups == [5, 4, 6, 7, 8, 9, 1, 3, 2])
    # cups = [int(c) for c in example1]
    print(perform_moves(cups, 10) == 92658374)
    print(perform_moves(cups, 100) == 67384529)

def get_solutions():
    cups = get_cups_from_file()
    print(perform_moves(cups, 100) == 96342875)


if __name__ == "__main__":
    begin = datetime.datetime.now()
    run_tests()
    get_solutions()
    end = datetime.datetime.now()
    print(end - begin)
