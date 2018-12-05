#[1518-06-02 23:58] Guard #859 begins shift
#[1518-07-13 00:56] falls asleep
#[1518-02-12 00:39] wakes up

def read_data(input):
    with open(input, 'r') as fin:
        lines = fin.readlines()
    messages = []
    for line in lines:
        year, month, day, hour, minute = int(line[1:5]), int(line[6:8]), int(line[9:11]), int(line[12:14]), int(line[15:17])
        time = minute + hour*60 + day*24*60 + month*30*24*60
        message = line.split(']')[1].split()
        if 'Guard' in message:
            sms = message[1]
        elif 'asleep' in message:
            sms = 'asleep'
        else:
            sms = 'wakes'
        messages.append([year, month, day, hour, minute,sms])
    messages.sort()
    return messages

def part1(input):
    guard = ''
    most = ['',0]
    db = {}
    for year, month, day, hour, minute, sms in input:
        if sms.startswith('#'):
            guard = sms
            if guard not in db:
                db[guard] = [0]*60 # 00:00 - 00:59
        elif sms == 'asleep':
            start = minute
        elif sms == 'wakes':
            for mins in range(start, minute):
                db[guard][mins] += 1
            if sum(db[guard]) > most[1]:
                most = [guard, sum(db[guard])]
    sleepy_guard, sleepy_time = most
    index = db[sleepy_guard].index(max(db[sleepy_guard]))
    return index * int(sleepy_guard.strip('#'))

def part2(input):
    guard = ''
    most = ['',0]
    db = {}
    for year, month, day, hour, minute, sms in input:
        if sms.startswith('#'):
            guard = sms
            if guard not in db:
                db[guard] = [0]*60 # 00:00 - 00:59
        elif sms == 'asleep':
            start = minute
        elif sms == 'wakes':
            for mins in range(start, minute):
                db[guard][mins] += 1
            if max(db[guard]) > most[1]:
                most = [guard, max(db[guard])]
    sleepy_guard, sleepy_time = most
    index = db[sleepy_guard].index(max(db[sleepy_guard]))
    return index * int(sleepy_guard.strip('#'))

input = 'day4.txt'
#input = 'test.txt'
data = read_data(input)
print(part1(data))
print(part2(data))