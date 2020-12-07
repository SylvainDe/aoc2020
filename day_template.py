def get_xxx_from_file(file_path="dayDAYNUMBER_input.txt"):
    with open(file_path) as f:
        return [l.strip() for l in f]


def run_tests():
    pass


def get_solutions():
    xxx = get_xxx_from_file()


if __name__ == "__main__":
    run_tests()
    get_solutions()
