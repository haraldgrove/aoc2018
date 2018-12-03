# Advent of code 2018
# Day 3
# Harald Grove
import sys
def part1(lines):
    # #1193 @ 567,208: 26x14
    sheet = {}
    for line in lines:
        try:
            id_, t, pos, size = line.strip().split()
        except ValueError:
            print(line)
            return
        pos = pos.strip(':').split(',')
        size = size.split('x')
        for x in range(int(pos[0]), int(pos[0])+int(size[0])):
            for y in range(int(pos[1]), int(pos[1])+int(size[1])):
                sheet[x,y] = sheet.get((x,y), 0) + 1
    count = 0
    for key, value in sheet.items():
        if value > 1:
            count += 1
    print(count)
    return sheet

def part2(lines, sheet):
    for line in lines:
        try:
            id_, t, pos, size = line.strip().split()
        except ValueError:
            print(line)
            return
        pos = pos.strip(':').split(',')
        size = size.split('x')
        overlap = False
        for x in range(int(pos[0]), int(pos[0])+int(size[0])):
            for y in range(int(pos[1]), int(pos[1])+int(size[1])):
                if sheet[x,y] > 1:
                    overlap = True
                    continue
            if overlap:
                break
        if not overlap:
            print(id_)

def read_data(input):
    with open(input, 'r') as fin:
        lines = fin.readlines()
    return lines

input = 'day3.txt'
#input = 'test.txt'
data = read_data(input)
sheet = part1(data)
part2(data, sheet)