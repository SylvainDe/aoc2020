def day1(file_path='day1_input.txt', target_sum=2020):
    with open(file_path) as f:
        nbs = set(int(l) for l in f)
    
    for n1 in nbs:
        n2 = target_sum - n1
        if n2 in nbs:
            return n1*n2

print(day1())
