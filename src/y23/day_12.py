with open('.\\src\\y23\\input\\day_12.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
grid = [list(line.strip()) for line in lines]

with open('.\\src\\y23\\input\\test.txt', 'r') as file:
    t_lines = [line.strip() for line in file.readlines()]
t_grid = [list(line.strip()) for line in t_lines]


print(t_grid)




def part1(input):
    sum = 0
    return sum


print(part1(t_grid))
print(part1(grid))

def part2(input):
    sum = 0
    return sum

print(part2(t_grid))
print(part2(grid))