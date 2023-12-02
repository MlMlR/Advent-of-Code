file_path = 'src\\y23\\input\\day_02.txt'
with open(file_path, 'r') as file:
    data = [line.strip() for line in file.readlines()]

file_path = 'src\\y23\\input\\test.txt'
with open(file_path, 'r') as file:
    test_data = [line.strip() for line in file.readlines()]

def part1(d):
    sum = 0
    for i, l in enumerate(d):
        fail = False
        game, results = l.split(":")
        results =results.replace("; ", ", ")
        for result in results.split(", "):
            result = result.strip()
            
            number, color = result.split(" ")
            if color == "red" and int(number) > 12:
                fail = True
            elif color == "green" and int(number) > 13:
                fail = True
            elif color == "blue" and int(number) > 14:
                fail = True
        if not fail:
            sum += i+1
        fail = False

    return sum

print(part1(test_data))


def part2(d):
    sum = 0
    for i, l in enumerate(d):
        r, g, b = 0, 0, 0 
        game, results = l.split(":")
        results =results.replace("; ", ", ")
        for result in results.split(", "):
            result = result.strip()
            number, color = result.split(" ")
            if color == "red":
                r = max(r, int(number))
            elif color == "green":
                g = max(g, int(number))
            elif color == "blue":
                b = max(b, int(number))
        sum += r*g*b
        r, g, b = 0, 0, 0 

    return sum

print(part2(test_data))

