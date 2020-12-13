def get_bus_information_from_file(file_path="day13_input.txt"):
    with open(file_path) as f:
        return get_bus_info(*[l for l in f])


def get_bus_info(line1, line2):
    return int(line1), [None if s == "x" else int(s) for s in line2.split(",")]


def get_wait_time_for_bus(ts, freq):
    p, q = divmod(ts, freq)
    return 0 if q == 0 else freq - q


def get_next_bus(bus_info):
    ts, buses = bus_info
    next_buses = [(b, get_wait_time_for_bus(ts, b)) for b in buses if b is not None]
    return min(next_buses, key=lambda b: b[1])


def run_tests():
    example1 = ["939", "7,13,x,x,59,x,31,19"]
    info = get_bus_info(example1[0], example1[1])
    nb, wait = get_next_bus(info)
    assert nb * wait == 295


def get_solutions():
    info = get_bus_information_from_file()
    nb, wait = get_next_bus(info)
    print(nb * wait)


if __name__ == "__main__":
    run_tests()
    get_solutions()
