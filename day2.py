import re

LINE_RE = re.compile(r"(?P<mini>\d+)-(?P<maxi>\d+) (?P<letter>.): (?P<pwd>.*)")

def line_is_valid_pwd(line):
    m = LINE_RE.fullmatch(line)
    if m is None:
        raise ValueError("Line did not match regular expression", line)
    mini, maxi, letter, pwd = m .groups()
    mini, maxi = int(mini), int(maxi)
    count = pwd.count(letter)
    return mini <= count <= maxi

def get_number_of_valid_pwd(file_path='day2_input.txt'):
    with open(file_path) as f:
        return sum(line_is_valid_pwd(l.strip()) for l in f)

# Examples provided
assert line_is_valid_pwd("1-3 a: abcde")
assert not line_is_valid_pwd("1-3 b: cdefg")
assert line_is_valid_pwd("2-9 c: ccccccccc")

# Real problem
print(get_number_of_valid_pwd() == 542)
