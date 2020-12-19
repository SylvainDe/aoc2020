# vi: set shiftwidth=4 tabstop=4 expandtab:


def get_data_from_file(file_path="day19_input.txt"):
    with open(file_path) as f:
        rules, strings = f.read().split("\n\n")
        return get_rules_from_string(rules), strings.split("\n")

quote = "\""
pipe = " | "

def get_rule_from_string(string):
    left, right = string.split(": ")
    left = int(left)
    if right.startswith(quote):
        assert right.endswith(quote)
        return left, right[1:-1]
    alternatives = right.split(pipe)
    return left, [[int(n) for n in alt.split()] for alt in alternatives]


def get_rules_from_string(string):
    rules = dict()
    for l in string.split("\n"):
        n, r = get_rule_from_string(l)
        rules[n] = r
    return rules

def seq_match_string(rules, seq, s):
    rems = [s]
    for e in seq:
        rems2 = []
        for rem in rems:
            for rem2 in rule_match_string(rules, rules[e], rem):
                rems2.append(rem2)
        if not rems2:
            return []
        rems = rems2
    return rems

def rule_match_string(rules, rule, s):
    # Either a literal string
    if isinstance(rule, str):
        if not s.startswith(rule):
            return []
        return [s[len(rule):]]
    # Or a list of alternatives
    return [rem for alt in rule for rem in seq_match_string(rules, alt, s)]


def rules_match_string(rules, s):
    return "" in rule_match_string(rules, rules[0], s)

def example1():
    rules = """0: 1 2
1: "a"
2: 1 3 | 3 1
3: "b\""""
    rules = get_rules_from_string(rules)
    for s in ["aab", "aba"]:
        print(rules_match_string(rules, s) == True)
    for s in ["aaa"]:
        print(rules_match_string(rules, s) == False)

def example2():
    rules = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b\""""
    rules = get_rules_from_string(rules)
    for s in ["aaaabb", "aaabab", "abbabb", "abbbab", "aabaab", "aabbbb", "abaaab", "ababbb"]:
        print(rules_match_string(rules, s) == True)
    for s in ["aaaabba", "aaababb", "abbbbb", "aabbab", "baabaab", "aaabbb", "ababab", "abaabbb"]:
        print(rules_match_string(rules, s) == False)

def run_tests():
    example1()
    example2()


def get_solutions():
    rules, strings = get_data_from_file()
    print(sum(rules_match_string(rules, s) for s in strings) == 118)
    new_rules = [
        "8: 42 | 42 8",
        "11: 42 31 | 42 11 31",
    ]
    for line in new_rules:
        n, r = get_rule_from_string(line)
        rules[n] = r
    print(sum(rules_match_string(rules, s) for s in strings) == 246)



if __name__ == "__main__":
    run_tests()
    get_solutions()
