input_file = open('data.txt', 'r')
data = input_file.read()

do_positions = [pos for pos, char in enumerate(data) if char == 'd' and data[pos:pos+4] == 'do()']
dont_positions = [pos for pos, char in enumerate(data) if char == 'd' and data[pos:pos+7] == "don't()"]
positions = [pos for pos, char in enumerate(data) if char == 'm' and data[pos:pos+4] == 'mul(']

result = 0

def find_closest_do_position(pos):
    x = 0
    for do_pos in do_positions:
        if do_pos < pos:
            x = do_pos
        if do_pos > pos:
            break
    return x

def find_closest_dont_position(pos):
    x = 0
    for dont_pos in dont_positions:
        if dont_pos < pos:
            x = dont_pos
        if dont_pos > pos:
            break
    return x

for pos in positions:
    do_pos = find_closest_do_position(pos)
    dont_pos = find_closest_dont_position(pos)
    if do_pos < dont_pos:
        continue

    comma = data.find(',', pos)
    end_bracket = data.find(')', pos)
    try:
        num1 = int(data[pos+4:comma])
        num2 = int(data[comma+1:end_bracket])
        if num1 > 999 or num2 > 999 or num1 < 0 or num2 < 0:
            continue

        result += num1 * num2
    except ValueError:
        continue

print(result)

