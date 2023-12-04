file_path = 'src\\y23\\input\\day_03.txt'
with open(file_path, 'r') as file:
    data = [line.strip() for line in file.readlines()]

file_path = 'src\\y23\\input\\test.txt'
with open(file_path, 'r') as file:
    test_data = [line.strip() for line in file.readlines()]

def part1(d):
    res = 0
    symbols = {'-', '+','&','/', '=', '#', '%', '$', '@', '*'}
    symbols = {'+', '#', '@', '/', '$', '&', '=', '*', '-', '%'}
    def has_adjacent_symbol(x, y):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(d) and 0 <= ny < len(d[0]):
                    if d[nx][ny] in symbols:
                        return True

        return False

    for i, row in enumerate(d):
        digits = ""
        indexes = []
        for col, val in enumerate(row):
            if val.isdigit():
                digits += val
                indexes.append(col)
            else :
                if digits != "":
                    skip = True
                    for index in indexes:
                        if has_adjacent_symbol(i, index):
                            skip = False
                    if not skip:
                        res += int(digits)
                digits = ""
                indexes = []
        
    return res
# between 536667 and 599598 not 399112

print(part1(test_data))
print(part1(data))




def part2(d):
    res = 0
    return res

print(part2(test_data))

def find_unique_characters(text):
    unique_chars = set()

    for l in text:
        for c in l:
            if not c.isdigit():
                unique_chars.add(c)


    print(unique_chars)

find_unique_characters(data)

def sum_part_numbers(schematic):
    # Define the symbols that count as adjacent to a part number
    symbols = {'+', '#', '@', '/', '$', '&', '=', '*', '-', '%'}
    
    # Convert the schematic into a 2D list for easier processing
    grid = [list(row) for row in schematic]

    # Helper function to check if a given position has an adjacent symbol
    def has_adjacent_symbol(x, y):
        # Check all adjacent positions (including diagonals)
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                # Skip checking the position of the number itself
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    if grid[nx][ny] in symbols:
                        return True
        return False

    # Initialize sum of part numbers
    sum_of_parts = 0

    # Iterate over each cell in the grid
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            # Check if the cell is a digit and has an adjacent symbol
            if isinstance(cell, int) and has_adjacent_symbol(i, j):
                # Extract the full number (which might span multiple digits)
                num = ''
                # Check digits to the left
                k = j
                while k >= 0 and grid[i][k].isdigit():
                    num = grid[i][k] + num
                    k -= 1
                # Check digits to the right
                k = j + 1
                while k < len(row) and grid[i][k].isdigit():
                    num += grid[i][k]
                    k += 1

                # Add the digit to the sum and mark these digits as processed
                sum_of_parts += int(num)
                for k in range(j, k):
                    grid[i][k] = 0

    return sum_of_parts

# Calculate the sum of part numbers in the schematic
sum_of_part_numbers = sum_part_numbers(test_data)
print(sum_of_part_numbers)
print(sum_of_part_numbers -114-58)
