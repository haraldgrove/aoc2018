import itertools
def part1(players, value):
    players = list(range(players))
    score = [0]*len(players)
    circle = [0, 2, 1]
    marble = 3
    current = 1
    for player in itertools.cycle(players):
        if player < 2 and len(circle) == 3:
            continue
        pos = (current + 2)
        if marble % 23 == 0:
            score[player] += marble
            current -= 7
            if current < 0:
                current += len(circle)
            score[player] += circle.pop(current)
            pos = current
        elif pos == len(circle):
            circle.append(marble)
        else:
            pos = pos % len(circle)
            circle.insert(pos,marble)
        current = pos
        #print(player, circle)
        marble += 1
        if marble == value+1:
            return max(score)
    return max(score)

from collections import deque
def part2(players, value):
    players = list(range(players))
    score = [0] * len(players)
    circle = deque([0])
    circle.append(1)
    circle.rotate(1)
    circle.append(2)
    marble = 3
    current = 2
    for player in itertools.cycle(players):
        if player < 2 and len(circle) == 3:
            continue
        if marble % 23 == 0:
            score[player] += marble
            circle.rotate(7)
            score[player] += circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)
        # print(player, circle)
        marble += 1
        if marble == value + 1:
            return max(score)
    return max(score)

def read_data(input):
    with open(input, 'r') as fin:
         l = next(fin).strip().split()
         players, value = int(l[0]), int(l[6])
    return players, value

input = 'day9.txt'
#input = 'test.txt'
player, value = read_data(input)
#print('part1:',part1(player, value))
print('part2:',part2(player, value*100))