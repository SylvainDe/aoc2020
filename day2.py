import re

LINE_RE = re.compile(r"(?P<mini>\d+)-(?P<maxi>\d+) (?P<letter>.): (?P<pwd>.*)")

def get_info_from_line(line):
    m = LINE_RE.fullmatch(line)
    if m is None:
        raise ValueError("Line did not match regular expression", line)
    mini, maxi, letter, pwd = m .groups()
    mini, maxi = int(mini), int(maxi)
    return (mini, maxi, letter, pwd)


def line_is_valid_pwd_part_1(line):
    mini, maxi, letter, pwd = get_info_from_line(line)
    count = pwd.count(letter)
    return mini <= count <= maxi

def get_number_of_valid_pwd_part1(file_path='day2_input.txt'):
    with open(file_path) as f:
        return sum(line_is_valid_pwd_part_1(l.strip()) for l in f)


def line_is_valid_pwd_part_2(line):
    mini, maxi, letter, pwd = get_info_from_line(line)
    return sum(pwd[pos-1] == letter for pos in (mini, maxi)) == 1

def get_number_of_valid_pwd_part2(file_path='day2_input.txt'):
    with open(file_path) as f:
        return sum(line_is_valid_pwd_part_2(l.strip()) for l in f)


# Examples provided
assert line_is_valid_pwd_part_1("1-3 a: abcde")
assert not line_is_valid_pwd_part_1("1-3 b: cdefg")
assert line_is_valid_pwd_part_1("2-9 c: ccccccccc")

assert line_is_valid_pwd_part_2("1-3 a: abcde")
assert not line_is_valid_pwd_part_2("1-3 b: cdefg")
assert not line_is_valid_pwd_part_2("2-9 c: ccccccccc")


# Real problem
print(get_number_of_valid_pwd_part1() == 542)
print(get_number_of_valid_pwd_part2() == 360)
