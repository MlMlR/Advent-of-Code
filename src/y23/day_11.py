with open('.\\src\\y23\\input\\day_11.txt', 'r') as file:
    data = [list(line.strip()) for line in file.readlines()]

with open('.\\src\\y23\\input\\test.txt', 'r') as file:
    test_d = [list(line.strip()) for line in file.readlines()]





def part1(input):
    sum = 0
    empty_rows = [r for r, row in enumerate(input) if all(cell != "#" for cell in row)]
    empty_cols = [c for c, col in enumerate(zip(*input)) if all(cell != "#" for cell in col)]
    points = [(r, c) for r, row in enumerate(input) for c, cell in enumerate(row) if cell == "#"]


    for i, (r1, c1) in enumerate(points):
        for r2, c2 in points[:i]:  
            # Add scaled value if row is empty, otherwise add 1
            for r in range(min(r1, r2), max(r1, r2)):
                sum += 2 if r in empty_rows else 1
            # Add scaled value if column is empty, otherwise add 1
            for c in range(min(c1, c2), max(c1, c2)):
                sum += 2 if c in empty_cols else 1

    return sum


print(part1(test_d))
print(part1(data))

def part2(input):
    sum = 0
    empty_rows = [r for r, row in enumerate(input) if all(cell == "." for cell in row)]
    empty_cols = [c for c, col in enumerate(zip(*input)) if all(cell == "." for cell in col)] 
    points = [(r, c) for r, row in enumerate(input) for c, cell in enumerate(row) if cell == "#"]


    for i, (r1, c1) in enumerate(points):
        for r2, c2 in points[:i]:  
            # Add scaled value if row is empty, otherwise add 1
            for r in range(min(r1, r2), max(r1, r2)):
                sum += 1000000 if r in empty_rows else 1
            # Add scaled value if column is empty, otherwise add 1
            for c in range(min(c1, c2), max(c1, c2)):
                sum += 1000000 if c in empty_cols else 1

    return sum

print(part2(test_d))
print(part2(data))