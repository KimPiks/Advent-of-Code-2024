input_file = open('data.txt', 'r')
data = input_file.readlines()
input_file.close()

data = [line.replace('\n', '') for line in data]

xmas_count = 0

def find_xmas(x1,x2,x3,x4,y1,y2,y3,y4):
    if x1 < 0 or x2 < 0 or x3 < 0 or x4 < 0 or y1 < 0 or y2 < 0 or y3 < 0 or y4 < 0:
        return 0
    if x1 >= len(data) or x2 >= len(data) or x3 >= len(data) or x4 >= len(data) or y1 >= len(data[0]) or \
            y2 >= len(data[0]) or y3 >= len(data[0]) or y4 >= len(data[0]):
        return 0

    if data[x1][y1] == 'X' and data[x2][y2] == 'M' and data[x3][y3] == 'A' and data[x4][y4] == 'S':
        return 1

    return 0

for x in range(len(data[0])):
    for y in range(len(data)):
        if data[x][y] == 'X':
            xmas_count += find_xmas(x, x-1, x-2, x-3, y, y, y, y)
            xmas_count += find_xmas(x, x+1, x+2, x+3, y, y, y, y)
            xmas_count += find_xmas(x, x, x, x, y, y-1, y-2, y-3)
            xmas_count += find_xmas(x, x, x, x, y, y+1, y+2, y+3)
            xmas_count += find_xmas(x, x-1, x-2, x-3, y, y-1, y-2, y-3)
            xmas_count += find_xmas(x, x+1, x+2, x+3, y, y+1, y+2, y+3)
            xmas_count += find_xmas(x, x-1, x-2, x-3, y, y+1, y+2, y+3)
            xmas_count += find_xmas(x, x+1, x+2, x+3, y, y-1, y-2, y-3)

print(xmas_count)