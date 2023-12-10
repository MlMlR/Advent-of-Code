import re

with open('.\\src\\y23\\input\\day_07.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]

with open('.\\src\\y23\\input\\test.txt', 'r') as file:
    test_d = [line.strip() for line in file.readlines()]


def is_five(s):
    return bool(re.search(r'(.)\1{4}', s))

def is_four(s):
    return bool(re.search(r'(.)\1{3}', s))

def is_full_house(s):
    return bool(re.search(r'(.)\1{2}(.)\2{1}', s)) or bool(re.search(r'(.)\1{1}(.)\2{2}', s))

def is_three(s):
    return bool(re.search(r'(.)\1{2}', s))

def is_two_pair(s):
    return bool(re.search(r'(.)\1{1}(.)\2{1}', s) or bool(re.search(r'((.)\2.*?(.)\3)', s)))

def is_one_pair(s):
    return bool(re.search(r'(.)\1{1}', s))



def part1(input):

    values = {
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'J': 10,
    'Q': 11,
    'K': 12,
    'A': 13
 }
    sum = 0
    five = []
    four = []
    full_house = []
    three = []
    two_pair = []
    one_pair = []
    high_card = []
    hands = {}

    for line in input:
        hand, bet = line.split(' ')
        hands[hand] = int(bet)
        sorted_string = ''.join(sorted(hand))
        if is_five(sorted_string):
            five.append(hand)
        elif is_four(sorted_string):
            four.append(hand)
        elif is_full_house(sorted_string):
            full_house.append(hand)
        elif is_three(sorted_string):
            three.append(hand)
        elif is_two_pair(sorted_string):
            two_pair.append(hand)
        elif is_one_pair(sorted_string):
            one_pair.append(hand)
        else:
            high_card.append(hand)
    
    sorte =[
        sorted(high_card, key=lambda s: [values[ch] for ch in s]),
        sorted(one_pair, key=lambda s: [values[ch] for ch in s]),
        sorted(two_pair, key=lambda s: [values[ch] for ch in s]),
        sorted(three, key=lambda s: [values[ch] for ch in s]),
        sorted(full_house, key=lambda s: [values[ch] for ch in s]),
        sorted(four, key=lambda s: [values[ch] for ch in s]),
        sorted(five, key=lambda s: [values[ch] for ch in s])
    ]
    i = 1
    for group in sorte:
        for hand in group:
            sum += hands[hand] * i
            i += 1
    return sum

print(part1(test_d))
print(part1(data))


def part2(input):
    values = {
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'J': 0,
    'Q': 11,
    'K': 12,
    'A': 13 
 }
    sum = 0
    five = []
    four = []
    full_house = []
    three = []
    two_pair = []
    one_pair = []
    high_card = []
    hands = {}

    for line in input:
        hand, bet = line.split(' ')
        hands[hand] = int(bet)
        sorted_string = ''.join(sorted(hand))
        if is_five(sorted_string):
            five.append(hand)
        elif is_four(sorted_string):
            if 'J' in sorted_string:
                five.append(hand)
            else:
                four.append(hand)
        elif is_full_house(sorted_string):
            if 'J' in sorted_string:
                five.append(hand)
            else:
                full_house.append(hand)
        elif is_three(sorted_string):
            if 'JJJ' in sorted_string:
                four.append(hand)
            elif 'J' in sorted_string:
                four.append(hand)
            else:
                three.append(hand)
        elif is_two_pair(sorted_string):
            if 'JJ' in sorted_string:
                four.append(hand)
            elif 'J' in sorted_string:
                full_house.append(hand)
            else:
                two_pair.append(hand)
        elif is_one_pair(sorted_string):
            if 'JJ' in sorted_string:
                three.append(hand)
            elif 'J' in sorted_string:
                three.append(hand)
            else:
                one_pair.append(hand)
        else:
            if 'J' in sorted_string:
                one_pair.append(hand)
            else:
                high_card.append(hand)
    
    sorte =[
        sorted(high_card, key=lambda s: [values[ch] for ch in s]),
        sorted(one_pair, key=lambda s: [values[ch] for ch in s]),
        sorted(two_pair, key=lambda s: [values[ch] for ch in s]),
        sorted(three, key=lambda s: [values[ch] for ch in s]),
        sorted(full_house, key=lambda s: [values[ch] for ch in s]),
        sorted(four, key=lambda s: [values[ch] for ch in s]),
        sorted(five, key=lambda s: [values[ch] for ch in s])
    ]
    i = 1
    for group in sorte:
        for hand in group:
            sum += hands[hand] * i
            i += 1
    return sum

print(part2(test_d))
print(part2(data))
# between ? and 244698637 not 244248840 or 244098371 or 243608487
#               243101568