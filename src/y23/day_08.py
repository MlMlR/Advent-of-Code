from math import gcd

file_path = 'src\\y23\\input\\day_08.txt'
with open(file_path, 'r') as file:
    data = [line.strip() for line in file.readlines()]

file_path = 'src\\y23\\input\\test.txt'
with open(file_path, 'r') as file:
    test_data = [line.strip() for line in file.readlines()]





def part1(lines):
    instructions = lines[0]
    network = {}

    for line in lines[2:]:
        node, connections = line.split(' = ')
        connections = tuple(connections.strip('()').split(', '))
        network[node.strip()] = connections

    current_node = 'AAA'
    step_count = 0

    while current_node != 'ZZZ':
        instruction = instructions[step_count % len(instructions)]
        current_node = network[current_node][0 if instruction == 'L' else 1]
        step_count += 1

    return step_count
print(part1(test_data) == 6)
print(part1(data))


def part2(lines):
    instructions = lines[0]
    network = {}
    for line in lines[2:]:
        node, connections = line.split(' = ')
        connections = tuple(connections.strip('()').split(', '))
        network[node.strip()] = connections

    start_nodes = [node for node in network if node.endswith('A')]
    step_counts = []

    for node in start_nodes:
        step_count = 0
        current_node = node
        while not current_node.endswith('Z'):
            instruction = instructions[step_count % len(instructions)]
            current_node = network[current_node][0 if instruction == 'L' else 1]
            step_count += 1
        step_counts.append(step_count)
    
    ggt = step_counts.pop()
    for count in step_counts:
        ggt = int(ggt * count / gcd(ggt, count))
    return ggt

print(part2(test_data))
print(part2(data))
