input_file = open('data.txt', 'r')
data = input_file.readlines()
input_file.close()

data = [line.replace('\n', '') for line in data]

xmas_count = 0

def find_xmas(x, y, horizontal):
    if x < 0 or y < 0:
        return 0
    if x >= len(data[0]) or y >= (len(data)):
        return 0

    count = 0

    if horizontal:
        if data[x + 1][y - 1] == 'A' and data[x][y - 2] == 'S' and data[x + 2][y - 2] == 'S':
            count += 1
        if (y + 2) < len(data) and data[x + 1][y + 1] == 'A' and data[x][y + 2] == 'S' and data[x + 2][y + 2] == 'S':
            count += 1
    else:
        if data[x - 1][y + 1] == 'A' and data[x - 2][y] == 'S' and data[x - 2][y + 2] == 'S':
            count += 1
        if x < (len(data[0])-2) and data[x + 1][y + 1] == 'A' and data[x + 2][y] == 'S' and data[x + 2][y + 2] == 'S':
            count += 1

    return count

for x in range(len(data[0])):
    for y in range(len(data)):
        if x < (len(data[0])-2) and  data[x][y] == 'M' and data[x+2][y] == 'M':
            xmas_count += find_xmas(x, y, True)

        if y < (len(data)-2) and data[x][y] == 'M' and data[x][y+2] == 'M':
            xmas_count += find_xmas(x, y, False)

print(xmas_count)