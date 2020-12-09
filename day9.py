def get_numbers_from_file(file_path="day9_input.txt"):
    with open(file_path) as f:
        return [int(l) for l in f]

def find_pair_sum(numbers, n):
    for p1 in numbers:
        p2 = n - p1
        if p2 in numbers:
            return True
    return False

def find_first_counterexample(numbers, preamble_size):
    for i in range(preamble_size, len(numbers)):
        n = numbers[i]
        if not find_pair_sum(set(numbers[i-preamble_size:i]), n):
            return n
    return None

def run_tests():
    example = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
    assert find_first_counterexample(example, 5) == 127


def get_solutions():
    numbers = get_numbers_from_file()
    print(find_first_counterexample(numbers, 25) == 70639851)

if __name__ == "__main__":
    run_tests()
    get_solutions()
