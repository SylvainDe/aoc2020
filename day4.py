def get_passport(string):
    data = dict()
    for chunk in string.split():
        key, value = chunk.split(":")
        assert key not in value
        data[key] = value
    return data

def get_passports(string):
    return [get_passport(s) for s in string.split("\n\n")]

def passport_is_valid(passport):
    keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    return all(key in passport for key in keys)


# Examples provided
example = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""
passports = get_passports(example)
assert passport_is_valid(passports[0])
assert not passport_is_valid(passports[1])
assert passport_is_valid(passports[2])
assert not passport_is_valid(passports[3])
assert sum(passport_is_valid(p) for p in passports) == 2

# Real problem
file_path='day4_input.txt'
with open(file_path) as f:
    passports = get_passports(f.read())
    print(sum(passport_is_valid(p) for p in passports) == 228)
