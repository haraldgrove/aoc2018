# Advent of code 2018
# Day 2
# Harald Grove

def part1(lines):
    count = [0,0]
    for line in lines:
        result = [line.count(a) for a in set(line)]
        if 2 in result:
            count[0] += 1
        if 3 in result:
            count[1] += 1
    print(count[0]*count[1])

def part2(lines):
    for ind1, line1 in enumerate(lines):
        for ind2, line2 in enumerate(lines):
            if ind2 <= ind1:
                continue
            diff = []
            for a,b in zip(line1,line2):
                if a != b:
                    diff.append(a)
            if len(diff) == 1:
                print(line1.strip())
                print(line2.strip())
                print(line1.strip().replace(diff[0],''))
                return


def read_data(input):
    with open(input, 'r') as fin:
        lines = fin.readlines()
    return lines

input = 'day2.txt'
data = read_data(input)
part1(data)
part2(data)