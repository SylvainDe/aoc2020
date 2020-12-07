import re


def get_rules_from_file(file_path="day7_input.txt"):
    with open(file_path) as f:
        return [get_rule_from_line(l.strip()) for l in f]


color_desc = r"[a-z]+ [a-z]+"
rule_re = re.compile(r"(?P<container>" + color_desc + ") bags contain (?P<content>.*).")
content_re = re.compile(r"(?P<number>\d+) (?P<color>" + color_desc + ") bags?")


def get_rule_from_line(line):
    m = rule_re.fullmatch(line)
    if m:
        lst = []
        container, content = m.groups()
        if content != "no other bags":
            for content_item in content.split(", "):
                m2 = content_re.fullmatch(content_item)
                if m2:
                    nb, color = m2.groups()
                    lst.append((int(nb), color))
                else:
                    print(content_item, "did not match")
        return container, lst
    else:
        print(m, "did not match")


def get_nb_colors_to_contain(rules, color):
    transitive_content = dict()
    can_be_in = dict()
    for c1, lst in rules:
        for _, c2 in lst:
            can_be_in.setdefault(c2, []).append(c1)

    reachable = set()
    to_process = set([color])
    while to_process:
        c1 = to_process.pop()
        reachable.add(c1)
        for c2 in can_be_in.get(c1, []):
            if c2 not in reachable:
                to_process.add(c2)
    return len(reachable) - 1


def run_tests():
    assert get_rule_from_line(
        "light red bags contain 1 bright white bag, 2 muted yellow bags."
    ) == ("light red", [(1, "bright white"), (2, "muted yellow")])
    assert get_rule_from_line("faded blue bags contain no other bags.") == (
        "faded blue",
        [],
    )
    examples1 = [
        "light red bags contain 1 bright white bag, 2 muted yellow bags.",
        "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
        "bright white bags contain 1 shiny gold bag.",
        "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
        "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
        "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
        "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
        "faded blue bags contain no other bags.",
        "dotted black bags contain no other bags.",
    ]
    rules = [get_rule_from_line(l) for l in examples1]
    assert get_nb_colors_to_contain(rules, "shiny gold") == 4


def get_solutions():
    rules = get_rules_from_file()
    print(get_nb_colors_to_contain(rules, "shiny gold") == 296)


if __name__ == "__main__":
    run_tests()
    get_solutions()
