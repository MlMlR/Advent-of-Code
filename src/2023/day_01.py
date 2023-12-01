file_path = 'input\\2023\\01.txt'
with open(file_path, 'r') as file:
    data = [line.strip() for line in file.readlines()]

def part1():
    print(sum(int(x[0] + x[-1]) for l in data if l for x in ([c for c in l if c.isdigit()],)))

part1()

def part2():
    ans = 0
    # Process each line in the provided data
    for line in data:
        digits = []
        for i, c in enumerate(line):
            if c.isdigit():
                digits.append(c)
            for d, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                if line[i:].startswith(val):
                    digits.append(str(d+1))  # d+1 because enumerate starts at 0

        # Calculate the score using the first and last digit found
        if digits:
            score = int(digits[0] + digits[-1])
            ans += score
    print(ans)

part2()