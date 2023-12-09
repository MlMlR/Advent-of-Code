file_path = '.\\src\\y23\\input\\day_09.txt'
with open(file_path, 'r') as file:
    data = [list(map(int, line.split())) for line in file.readlines()]

file_path = '.\\src\\y23\\input\\test.txt'
with open(file_path, 'r') as file:
    test_data = [list(map(int, line.split())) for line in file.readlines()]


def last_one(line):
    # calculate the differences of entries in the array
    diff = [line[i+1] - line[i] for i in range(len(line)-1)]
    if sum(diff) == 0:
        return line[-1]
    return last_one(diff) + line[-1]


def part1(input):
    res = 0
    for line in input:
       res += last_one(line)

    return res


print(part1(test_data) == 114)
print(part1(data))



def previous(line):
    # calculate the differences of entries in the array
    diff = [line[i+1] - line[i] for i in range(len(line)-1)]
    if sum(diff) == 0:
        return line[0]
    return line[0] - previous(diff)


def part2(input):
    res = 0
    for line in input:
       res += previous(line)

    return res


print(part2(test_data) == 2)
print(part2(data))