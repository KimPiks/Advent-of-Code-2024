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

similarity_score = 0
for i in range(len(first_list)):
    similarity_score += int(first_list[i]) * second_list.count(first_list[i])

print(similarity_score)