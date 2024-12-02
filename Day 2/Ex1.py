input_file = open("data.txt", 'r')
data = input_file.readlines()
input_file.close()

safe_reports_count = 0

def is_monotonic(array):
    return all(array[i] < array[i + 1] for i in range(len(array) - 1)) or \
           all(array[i] > array[i + 1] for i in range(len(array) - 1))

def is_safe(array):
    mono = is_monotonic(array)
    if not mono:
        return False

    diff = all(abs(array[i + 1] - array[i]) <= 3 for i in range(len(array) - 1))
    return diff

for line in data:
    numbers = line.split()
    numbers = [int(x) for x in numbers]
    if is_safe(numbers):
        safe_reports_count += 1


print(safe_reports_count)