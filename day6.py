def get_groups_from_file(file_path="day6_input.txt"):
    with open(file_path) as f:
        return get_groups_from_string(f.read())

def get_groups_from_string(string):
    return [s.split() for s in string.split("\n\n")]

def get_sum_of_any_yes_answers(groups):
    return sum(len(set("".join(g))) for g in groups)

def get_sum_of_all_yes_answers(groups):
    return sum(len(set(g[0]).intersection(*g)) for g in groups)

def run_tests():
    example1 = """abc

a
b
c

ab
ac

a
a
a
a

b"""
    groups = get_groups_from_string(example1)
    assert get_sum_of_any_yes_answers(groups) == 11
    assert get_sum_of_all_yes_answers(groups) == 6


def get_solutions():
    groups = get_groups_from_file()
    print(get_sum_of_any_yes_answers(groups) == 6416)
    print(get_sum_of_all_yes_answers(groups) == 3050)


if __name__ == "__main__":
    run_tests()
    get_solutions()
