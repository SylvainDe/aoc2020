import collections
import itertools

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

def get_nb_charging_arrangements(adapters):
    chunks = []
    adapters = sorted(adapters + [max(adapters) + 3])
    chunk = []
    prev = 0
    for ad in adapters:
        diff = ad - prev
        if diff > 3:
            return 0
        elif diff == 3:
            chunks.append(chunk + [ad])
            chunk = [ad]
        else:
            chunk.append(ad)
        prev = ad
    ret = 1
    for c in chunks:
        nb = get_nb_charging_arrangements_internal(c)
        ret *= nb
    return ret


def powerset(iterable):
    # From https://docs.python.org/3/library/itertools.html#itertools-recipes
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

def get_nb_charging_arrangements_internal(adapters):
    nb = 0
    beg, last = adapters[0], adapters[-1]
    for ad in powerset(adapters[1:-1]):
        candidates = [beg] + list(ad) + [last]
        nb += all(second - first <= 3 for first, second in zip(candidates, candidates[1:]))
    return nb


def run_tests():
    example1 = [ 16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    example2 = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]

    jolt_diff = get_jolt_differences(example1)
    assert jolt_diff[1] * jolt_diff[3] == 35
    jolt_diff = get_jolt_differences(example2)
    assert jolt_diff[1] * jolt_diff[3] == 220

    print(get_nb_charging_arrangements(example1) == 8)
    print(get_nb_charging_arrangements(example2)) # should be 19208


def get_solutions():
    adapters = get_adapters_from_file()
    jolt_diff = get_jolt_differences(adapters)
    print(jolt_diff[1] * jolt_diff[3] == 1656)
    print(get_nb_charging_arrangements(adapters)) # should be more than 32396521357312


if __name__ == "__main__":
    run_tests()
    get_solutions()
