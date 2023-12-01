file_path = '.\\src\\y23\\input\\day_01.txt'
with open(file_path, 'r') as file:
    data = [line.strip() for line in file.readlines()]

def part1(d):
    """
    Sums the first and last digits from each line of the input data.
    Lines without digits will contribute 0 to the sum.

    Parameters:
    - data (str): A multiline string with each line potentially containing digits.

    Returns:
    - int: The total sum of the calibration values.
    """
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