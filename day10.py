def printpattern(second, lines):
    db = {}
    minx,maxx,miny,maxy = lines[0][0][0],lines[0][0][0],lines[0][0][1],lines[0][0][1]
    for pos, vel in lines:
        db[pos[0],pos[1]] = 1
        minx = min(minx, pos[0])
        miny = min(miny, pos[1])
        maxx = max(maxx, pos[0])
        maxy = max(maxy, pos[1])
    if maxx - minx > 200:
        return (maxx - minx)
    with open('pattern.txt', 'a') as fout:
        fout.write(str(second)+'\n')
        for y in range(miny, maxy+1):
            for x in range(minx, maxx+1):
                if (x,y) in db:
                    fout.write('#')
                else:
                    fout.write('.')
            fout.write('\n')
    return maxx-minx

def part1(lines):
    second = 1
    finished = False
    size = printpattern(second,lines)
    while not finished:
        for pos, vel in lines:
            pos[0] += vel[0]
            pos[1] += vel[1]
        size = printpattern(second, lines)
        if size < 200:
            finished = True
        elif finished and size > 200:
            return
        second += 1


def part2(lines):
    pass

def read_data(input):
    lines = []
    with open(input, 'r') as fin:
        for line in fin:
            line = line.replace('<',',').replace('>',',')
            l = line.strip().split(',')
            pos = [int(l[1]), int(l[2])]
            vel = [int(l[4]), int(l[5])]
            lines.append([pos, vel])
    return lines

input = 'day10.txt'
#input = 'test.txt'
indata = read_data(input)
# The solution require manually checking the output for the message
print('part1:',part1(indata))
# Get the time spent from the pattern in part1
print('part2:',part2(indata))