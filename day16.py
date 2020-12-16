# vi: set shiftwidth=4 tabstop=4 expandtab:
import re

rules_re = re.compile(r"(?P<min>\d+)-(?P<max>\d+)")
def get_rule_from_string(string):
    name, values = string.split(": ")
    return (name, [(int(mini), int(maxi)) for mini, maxi in rules_re.findall(values)])

def get_ticket_from_string(string):
    return [int(n) for n in string.split(",")]

def get_info_from_string(string):
    rules, ticket, tickets = string.split("\n\n")
    return ([get_rule_from_string(r) for r in rules.split("\n")],
            get_ticket_from_string(ticket.split("\n")[1]),
            [get_ticket_from_string(s) for s in tickets.split("\n")[1:] if s])


def get_info_from_file(file_path="day16_input.txt"):
    with open(file_path) as f:
        return get_info_from_string(f.read())


def value_valid_for_a_field(rules, n):
    return any(mini <= n <= maxi for _, lst in rules for mini, maxi in lst)

def validity_rate(rules, tickets):
    return sum(n for t in tickets for n in t if not value_valid_for_a_field(rules, n))

def run_tests():
    example1 = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""
    rules, ticket, tickets = get_info_from_string(example1)
    assert rules == [('class', [(1, 3), (5, 7)]), ('row', [(6, 11), (33, 44)]), ('seat', [(13, 40), (45, 50)])]
    assert ticket == [7, 1, 14]
    assert tickets == [[7, 3, 47], [40, 4, 50], [55, 2, 20], [38, 6, 12]]
    assert validity_rate(rules, tickets)

def get_solutions():
    rules, ticket, tickets = get_info_from_file()
    print(validity_rate(rules, tickets))


if __name__ == "__main__":
    run_tests()
    get_solutions()
