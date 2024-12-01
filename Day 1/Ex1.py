input_file = open("data.txt", 'r')
data = input_file.readlines()
input_file.close()

first_list = []
second_list = []

for line in data:
    x = line.split()[0]
    y = line.split()[1]

    first_list.append(x)
    second_list.append(y)

first_list.sort()
second_list.sort()

total_distance = 0
for i in range(len(first_list)):
    total_distance += abs(int(first_list[i]) - int(second_list[i]))

print(total_distance)