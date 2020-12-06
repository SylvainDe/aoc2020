import day1, day2, day3, day4, day5, day6

days = [day1, day2, day3, day4, day5, day6]


def run_tests():
    for day in days:
        print("-", day.__name__)
        day.run_tests()


def get_solutions():
    for day in days:
        print("-", day.__name__)
        day.get_solutions()


if __name__ == "__main__":
    run_tests()
    get_solutions()
