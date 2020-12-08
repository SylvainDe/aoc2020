def get_program_from_file(file_path="day8_input.txt"):
    with open(file_path) as f:
        return [l.strip() for l in f]

def get_instruction(string):
    op, arg = string.split()
    return op, int(arg)

def get_state_after(program, pos, acc):
    op, arg = get_instruction(program[pos]) 
    if op == "nop":
        return pos + 1, acc
    elif op == "jmp":
        return pos + arg, acc
    elif op == "acc":
        return pos + 1, acc + arg
    raise ValueError("Invalid op:", op)

def run_program_until_loop(program):
    pos, acc = 0, 0
    visited = set([pos])
    while True:
        pos, acc = get_state_after(program, pos, acc)
        if pos in visited:
            return acc
        visited.add(pos)

def run_tests():
    example1 = [
        "nop +0",
        "acc +1",
        "jmp +4",
        "acc +3",
        "jmp -3",
        "acc -99",
        "acc +1",
        "jmp -4",
        "acc +6",
    ]
    assert run_program_until_loop(example1) == 5


def get_solutions():
    program = get_program_from_file()
    print(run_program_until_loop(program) == 1521)

if __name__ == "__main__":
    run_tests()
    get_solutions()
