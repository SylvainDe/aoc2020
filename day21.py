# vi: set shiftwidth=4 tabstop=4 expandtab:
import datetime


def get_ingredients_from_line(line):
    beg, sep, end = line.partition(" (contains ")
    return tuple(beg.split(" ")), end[:-1].split(", ")


def get_ingredients_from_file(file_path="day21_input.txt"):
    with open(file_path) as f:
        return [get_ingredients_from_line(l.strip()) for l in f]


def find_safe_ingredient(ingredients):
    identified_ingredients = dict()
    identified_alergens = dict()
    change = True
    while change:
        change = False
        alergen_sources = dict()
        for ingred, alergens in ingredients:
            for a in alergens:
                if a not in identified_alergens:
                    alergen_sources.setdefault(a, []).append(
                        tuple(i for i in ingred if i not in identified_ingredients)
                    )
        for a, meta_list in alergen_sources.items():
            cand = set.intersection(*[set(l) for l in meta_list])
            if len(cand) == 1:
                i = cand.pop()
                identified_ingredients[i] = a
                identified_alergens[a] = i
                change = True
    return sum(
        i not in identified_ingredients for ingred, _ in ingredients for i in ingred
    )


def run_tests():
    example1 = [
        "mxmxvkd kfcds sqjhc nhms (contains dairy, fish)",
        "trh fvjkl sbzzf mxmxvkd (contains dairy)",
        "sqjhc fvjkl (contains soy)",
        "sqjhc mxmxvkd sbzzf (contains fish)",
    ]
    ingredients = [get_ingredients_from_line(l) for l in example1]
    assert find_safe_ingredient(ingredients) == 5


def get_solutions():
    ingredients = get_ingredients_from_file()
    print(find_safe_ingredient(ingredients) == 2317)


if __name__ == "__main__":
    begin = datetime.datetime.now()
    run_tests()
    get_solutions()
    end = datetime.datetime.now()
    print(end - begin)
