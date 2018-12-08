

def part1(numbers, node):
    children, meta, numbers = numbers[0], numbers[1], numbers[2:]
    for child in range(children):
        numbers = part1(numbers, node+1)
    results.extend([n for n in numbers[0:meta]])
    return numbers[meta:]


def part2(numbers, node):
    children, meta, numbers = numbers[0], numbers[1], numbers[2:]
    if children == 0:
        return sum(numbers[0:meta]), numbers[meta:]
    values = []
    for child in range(children):
        value, numbers = part2(numbers, node+1)
        values.append(value)
    metadata = numbers[0:meta]
    value = sum([values[m-1] for m in metadata if m > 0 and m < len(values)+1])
    return value, numbers[meta:]


def read_data(input):
    with open(input, 'r') as fin:
        numbers = tuple(map(int, next(fin).strip().split()))
    return numbers

input = 'day8.txt'
results = []
indata = read_data(input)
part1(indata, 0)
print('part1:',sum(results))
tree = {}
print('part2:',part2(indata, 0)[0])