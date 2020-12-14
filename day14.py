import re


def get_program_from_file(file_path="day14_input.txt"):
    with open(file_path) as f:
        return [l.strip() for l in f]


# mask = X100110110X011000101000101XX11001X11
mask_re = re.compile(r"^mask = (?P<mask>[01X]+)$")
# mem[5201] = 1838761
mem_re = re.compile(r"^mem\[(?P<addr>\d+)\] = (?P<value>\d+)")


def apply_mask(value, mask):
    value = format(value, "0%db" % len(mask))
    bits = []
    for bv, mv in zip(value, mask):
        bits.append(bv if mv == "X" else mv)
    return int("".join(bits), 2)


def run_program(program):
    mask = ""
    memory = dict()
    for line in program:
        m_mask = mask_re.fullmatch(line)
        if m_mask is not None:
            d = m_mask.groupdict()
            mask = d["mask"]
        else:
            m_mem = mem_re.fullmatch(line)
            if m_mem is not None:
                d = m_mem.groupdict()
                memory[int(d["addr"])] = apply_mask(int(d["value"]), mask)
            else:
                raise ValueError(line)
    return sum(v for v in memory.values())


def run_tests():
    example1 = [
        "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
        "mem[8] = 11",
        "mem[7] = 101",
        "mem[8] = 0",
    ]
    assert apply_mask(11, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X") == 73
    assert apply_mask(101, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X") == 101
    assert apply_mask(0, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X") == 64
    assert run_program(example1) == 165


def get_solutions():
    program = get_program_from_file()
    print(run_program(program))


if __name__ == "__main__":
    run_tests()
    get_solutions()
