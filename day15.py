def get_numbers_from_file(file_path="day15_input.txt"):
    with open(file_path) as f:
        for l in f:
            return [int(s) for s in l.split(",")]


def play_game(numbers, turn):
    if turn <= len(numbers):
        return numbers[turn - 1]
    ages = dict()
    for i, n in enumerate(numbers):
        ages.setdefault(n, []).append(i)
    n = numbers[-1]
    for i in range(len(numbers), turn):
        lst_ages = ages[n]
        if len(lst_ages) == 1:
            n = 0
        else:
            n = lst_ages[-1] - lst_ages[-2]
        ages.setdefault(n, []).append(i)
    return n


def run_tests():
    example1 = [0, 3, 6]
    assert play_game(example1, 1) == 0
    assert play_game(example1, 9) == 4
    assert play_game(example1, 10) == 0
    assert play_game(example1, 2020) == 436


#    assert play_game(example1, 30000000) == 175594 - slow


def get_solutions():
    numbers = get_numbers_from_file()
    print(play_game(numbers, 2020) == 273)


#    print(play_game(numbers, 30000000) == 47205) - slow


if __name__ == "__main__":
    run_tests()
    get_solutions()
