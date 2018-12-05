import sys
def part1(data):
    pos = 0
    while pos < len(data)-1:
        a, b = data[pos],data[pos+1]
        if abs(ord(a)-ord(b)) == 32:
            data = data[0:pos]+data[pos+2:]
            pos -= 1
        else:
            pos += 1
    return len(data)


    
def part2(rawdata):
    #print('total length', len(rawdata))
    data = rawdata[:]
    aminos = set(data.lower())
    maks = ['',len(rawdata)]
    for amino in aminos:
        #print('current:', amino)
        data = rawdata[:]
        #print('lower',data.count(amino), 'upper', data.count(amino.upper()))
        data = data.replace(amino, '')
        data = data.replace(amino.upper(), '')
        #print('length after removal:', len(data))
        pos = 0
        while pos < len(data) - 1:
            try:
                a, b = data[pos], data[pos + 1]
            except IndexError:
                print(pos, len(data))
                sys.exit(1)
            if abs(ord(a) - ord(b)) == 32:
                data = data[0:pos] + data[pos + 2:]
                if pos > 0:
                    pos -= 1
                if len(data) < 2:
                    return 1
            else:
                pos += 1
        if len(data) < maks[1]:
            maks = [amino, len(data)]
    return maks[1]


def read_data(input):
    with open(input, 'r') as fin:
        lines = fin.read().strip()
    return lines


input = 'day5.txt'
#input = 'day5_debug.txt'
#input = 'test.txt'
indata = read_data(input)
print('part1:', part1(indata))
print('part2:', part2(indata))