import numpy as np

def manhattan(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

def infinite(area, p1):
    edgey, edgex = area.shape
    value = area[p1[1], p1[0]]
    x,y, *_ = p1
    if x == 0 or y == 0 or x == edgex-1 or y == edgey-1:
        return True
    while True:
        y -= 1
        if np.isnan(area[y,x]) or area[y,x] != value:
            break
        if y == 0:
            return True
    x, y, *_ = p1
    while True:
        y += 1
        if np.isnan(area[y, x]) or area[y, x] != value:
            break
        if y == edgey-1:
            return True
    x, y, *_ = p1
    while True:
        x -= 1
        if np.isnan(area[y, x]) or area[y, x] != value:
            break
        if x == 0:
            return True
    x, y, *_ = p1
    while True:
        x += 1
        if np.isnan(area[y, x]) or area[y, x] != value:
            break
        if x == edgex-1:
            return True
    return False

def part1(data):
    area, points, xadj, yadj = data
    ylen, xlen = area.shape
    for y in range(ylen):
        for x in range(xlen):
            if area[y,x] == 0:
                md = sorted([(manhattan((x,y), p2),p2[2]) for p2 in points])
                if md[0][0] == md[1][0]:
                    area[y,x] = np.nan
                else:
                    area[y,x] = md[0][1]
    bounded = []
    valid = set()
    for point in points:
        if not infinite(area, point):
            bounded.append(point)
            valid.add(point[2])
    #print(bounded, valid)
    maks = 0
    for point in bounded:
        sq = len(area[np.where(area == point[2])])
        maks = max(maks, sq)
    return maks

def part2(data):
    area, points, xadj, yadj = data
    ylen, xlen = area.shape
    for y in range(ylen):
        for x in range(xlen):
            area[y,x] = sum([manhattan((x, y), p2) for p2 in points])
    sq = len(area[np.where(area < 10000)])
    return sq

def read_data(input):
    n = e = s = w = None
    points = []
    with open(input, 'r') as fin:
        rank = 1
        for line in fin:
            x,y = line.strip().split(',')
            x = int(x)
            y = int(y)
            points.append((x,y,rank))
            rank += 1
            if n is None:
                n, e, s, w = y, x, y, x
                continue
            n = min(n, y)
            e = max(e, x)
            s = max(s, y)
            w = min(w, x)
    ydiff = 1+s-n
    xdiff = 1+e-w
    area = np.zeros((ydiff,xdiff))
    xadj, yadj = w, n
    newpoints = []
    for x,y,rank in points:
        x -= xadj
        y -= yadj
        area[y,x] = rank
        newpoints.append((x,y,rank))
    return area, newpoints, xadj, yadj

input = 'day6.txt'
#input = 'test.txt'
indata = read_data(input)
print('part1:', part1(indata))
print('part2:', part2(indata))