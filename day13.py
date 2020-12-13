import math


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


def get_lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def get_next_timestamp_with_offsets(buses):
    buses = [(i, b) for i, b in enumerate(buses) if b is not None]
    ts = 0
    lcm = 1
    for i, b in buses:
        while True:
            if (ts + i) % b == 0:
                break
            ts += lcm
        lcm = get_lcm(lcm, b)
    return ts


def run_tests():
    example1 = ["939", "7,13,x,x,59,x,31,19"]
    info = get_bus_info(example1[0], example1[1])
    nb, wait = get_next_bus(info)
    assert nb * wait == 295
    assert get_next_timestamp_with_offsets(info[1]) == 1068781
    assert get_next_timestamp_with_offsets([17, None, 13, 19]) == 3417
    assert get_next_timestamp_with_offsets([67, 7, 59, 61]) == 754018
    assert get_next_timestamp_with_offsets([67, None, 7, 59, 61]) == 779210
    assert get_next_timestamp_with_offsets([67, 7, None, 59, 61]) == 1261476
    assert get_next_timestamp_with_offsets([1789, 37, 47, 1889]) == 1202161486


def get_solutions():
    info = get_bus_information_from_file()
    nb, wait = get_next_bus(info)
    print(nb * wait == 2845)
    print(get_next_timestamp_with_offsets(info[1]) == 487905974205117)


if __name__ == "__main__":
    run_tests()
    get_solutions()
