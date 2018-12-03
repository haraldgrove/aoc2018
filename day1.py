# Advent of code 2018
# Day 1
# Harald Grove

def part1(changes):
    freq = 0
    with open('day1.txt', 'r') as fin:
        for line in changes:
            change_freq = int(line)
            freq += change_freq
    print(freq)

def part2(changes):
    # Itertools cycle should have been used here
    freq = 0
    db_freq = set()
    while True:
        for ch in changes:
            freq += int(ch)
            if freq in db_freq:
                print(freq)
                return
            db_freq.add(freq)

def read_data(input):
    with open(input, 'r') as fin:
        changes = fin.readlines()
    return changes

input = 'day1.txt'
data = read_data(input)
part1(data)
part2(data)