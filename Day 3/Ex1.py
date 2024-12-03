input_file = open('data.txt', 'r')
data = input_file.read()

positions = [pos for pos, char in enumerate(data) if char == 'm' and data[pos:pos+4] == 'mul(']

result = 0

for pos in positions:
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

