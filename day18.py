# vi: set shiftwidth=4 tabstop=4 expandtab:


def get_expr_from_file(file_path="day18_input.txt"):
    with open(file_path) as f:
        return [l.strip() for l in f]


def eval_expr(expr):
    if not expr:
        return 0
    for i, c in reversed(list(enumerate(expr))):
        if c in ("+", "*", "-", ")"):
            lhs, rhs = expr[:i], expr[i + 1 :]
            if c == "+":
                return eval_expr(lhs) + int(rhs)
            if c == "-":
                return eval_expr(lhs) - int(rhs)
            elif c == "*":
                return eval_expr(lhs) * int(rhs)
            elif c == ")":
                nb_parenth = 1
                for j, c2 in reversed(list(enumerate(lhs))):
                    if c2 == ")":
                        nb_parenth += 1
                    elif c2 == "(":
                        nb_parenth -= 1
                        if nb_parenth == 0:
                            rem, inside_paren = lhs[:j], lhs[j + 1 :]
                            return eval_expr(rem + str(eval_expr(inside_paren)) + rhs)
                raise ValueError("Unmatched parenthesis in %s" % expr)
    val = int(expr)
    return val


def eval_expr2(expr):
    # print(expr)
    if not expr:
        return 0
    for i, c in enumerate(expr):
        lhs, rhs = expr[:i], expr[i + 1 :]
        if c == "(":
            # print("expr:'%s': '%s', '%s', '%s'" % (expr, lhs, c, rhs))
            nb_parenth = 1
            for j, c2 in enumerate(rhs):
                if c2 == "(":
                    nb_parenth += 1
                elif c2 == ")":
                    nb_parenth -= 1
                    if nb_parenth == 0:
                        inside_paren, rem = rhs[:j], rhs[j + 1 :]
                        # print("rhs:'%s': '%s' '%s'" % (rhs, inside_paren, rem))
                        return eval_expr2(lhs + str(eval_expr2(inside_paren)) + rem)
            raise ValueError("Unmatched parenthesis in %s" % expr)
        elif c == "*":
            return eval_expr2(lhs) * eval_expr2(rhs)
    for i, c in enumerate(expr):
        lhs, rhs = expr[:i], expr[i + 1 :]
        if c in ("+", "-"):
            lhs = int(lhs) if lhs else 0
            if c == "+":
                return lhs + eval_expr2(rhs)
            elif c == "-":
                return lhs - eval_expr2(rhs)
    val = int(expr)
    return val


def run_tests():
    # My tests
    assert eval_expr("2 + 3") == 5
    assert eval_expr("2 * 3") == 6
    assert eval_expr("3 - 2") == 1
    assert eval_expr("+2") == 2
    assert eval_expr("-3") == -3
    assert eval_expr("(2)") == 2
    assert eval_expr("((((2))))") == 2
    assert eval_expr("1 + 2 * 3") == 9
    # Tests provided
    assert eval_expr("1 + 2 * 3 + 4 * 5 + 6") == 71
    assert eval_expr("1 + (2 * 3) + (4 * (5 + 6))") == 51
    assert eval_expr("2 * 3 + (4 * 5)") == 26
    assert eval_expr("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 437
    assert eval_expr("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 12240
    assert eval_expr("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 13632
    # My tests
    print(eval_expr2("2 + 3") == 5)
    print(eval_expr2("2 * 3") == 6)
    print(eval_expr2("3 - 2") == 1)
    print(eval_expr2("+2") == 2)
    print(eval_expr2("-3") == -3)
    print(eval_expr2("(2)") == 2)
    print(eval_expr2("((((2))))") == 2)
    print(eval_expr2("1 + 2 * 3") == 9)

    print(eval_expr2("1 + (2 * 3) + (4 * (5 + 6))"))  # still becomes 51.
    print(eval_expr2("2 * 3 + (4 * 5)"))  # becomes 46.
    print(eval_expr2("5 + (8 * 3 + 9 + 3 * 4 * 3)"))  # becomes 1445.
    print(eval_expr2("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"))  # becomes 669060.
    print(
        eval_expr2("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2")
    )  # becomes 23340.


def get_solutions():
    expr = get_expr_from_file()
    print(sum(eval_expr(e) for e in expr) == 53660285675207)
    print(sum(eval_expr2(e) for e in expr) == 141993988282687)


if __name__ == "__main__":
    run_tests()
    get_solutions()
