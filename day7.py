def find_next(db, order):
    options = []
    for key in db:
        if len(db[key]['before']) == 0:
            options.append(key)
    return sorted(options)[0]

def prunedb(db, s):
    for key in db:
        try:
            ind = db[key]['before'].index(s)
        except ValueError:
            continue
        del db[key]['before'][ind]

def part1(lines):
    db = {}
    for a,b in lines:
        if a not in db:
            db[a] = {'before':[], 'after':[]}
        if b not in db:
            db[b] = {'before':[], 'after':[]}
        db[a]['after'].append(b)
        db[b]['before'].append(a)
    order = ''
    while len(db) > 0:
        if len(order) > 0:
            prunedb(db, order[-1])
        letter = find_next(db, order)
        order += letter
        del db[letter]
    return order

def find_next2(db, base):
    options = []
    for key in db:
        if len(db[key]['before']) == 0 and not db[key]['assigned']:
            options.append(key)
    if len(options) == 0:
        return None
    job = sorted(options)[0]
    db[job]['assigned'] = True
    return job

def part2(lines, base, workers):
    db = {}
    for a, b in lines:
        if a not in db:
            db[a] = {'before': [], 'after': [], 'completed':base+ord(a)-64, 'assigned':False}
        if b not in db:
            db[b] = {'before': [], 'after': [], 'completed':base+ord(b)-64, 'assigned':False}
        db[a]['after'].append(b)
        db[b]['before'].append(a)
    # Work assignment
    worker = [None]* workers
    second = 0
    while True:
        for i, job in enumerate(worker):
            if job is not None:
                continue
            letter = find_next2(db, base)
            worker[i] = letter
        #print(worker)
        for i, job in enumerate(worker):
            if job is None:
                continue
            db[job]['completed'] -= 1
            if db[job]['completed'] == 0:
                del db[job]
                prunedb(db,job)
                worker[i] = None
                if len(db) == 0:
                    return second+1
        second += 1

def read_data(input):
    lines = []
    with open(input, 'r') as fin:
        for line in fin:
            l = line.strip().split()
            a, b = l[1], l[7]
            lines.append((a,b))
    return lines

input, workers, base = 'day7.txt', 5, 60
#input, workers = 'test.txt', 2, 0
indata = read_data(input)
#print('part1:', part1(indata))
print('part2:', part2(indata, base, workers))