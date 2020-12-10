import collections

def get_adapters_from_file(file_path="day10_input.txt"):
    with open(file_path) as f:
        return [int(l) for l in f]

def get_jolt_differences(adapters):
    adapters = sorted(adapters)
    differences = []
    prev = 0
    for ad in adapters:
        differences.append(ad - prev)
        prev = ad
    differences.append(3)
    return collections.Counter(differences)

def run_tests():
    example1 = [ 16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    jolt_diff = get_jolt_differences(example1)
    print(jolt_diff[1] * jolt_diff[3])
    # TODO: Add example 2


def get_solutions():
    adapters = get_adapters_from_file()
    jolt_diff = get_jolt_differences(adapters)
    print(jolt_diff[1] * jolt_diff[3])


if __name__ == "__main__":
    run_tests()
    get_solutions()
