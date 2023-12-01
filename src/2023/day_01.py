file_path = 'input\\2023\\01.txt'
with open(file_path, 'r') as file:
    data = [line.strip() for line in file.readlines()]

def part1(d):
    print(sum(int(x[0] + x[-1]) for l in d if l for x in ([c for c in l if c.isdigit()],)))

part1(data)

def part2(d):
    z = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    S = 0
    for l in d:
        dg = []
        for i, c in enumerate(l):
            if c.isdigit():
                dg.append(c)
            for d, v in enumerate(z):
                if l[i:].startswith(v):
                    dg.append(str(d+1))
        if dg:
            x = int(dg[0] + dg[-1])
            S += x
    print(S)

part2(data)