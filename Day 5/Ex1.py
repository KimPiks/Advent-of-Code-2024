f = open("data.txt", "r")
lines = f.readlines()
f.close()

rules_1 = []
rules_2 = []
updates = []

read_updates = False
for line in lines:
    if line == "\n":
        read_updates = True
        continue

    if read_updates:
        updates.append(line.strip())
    else:
        rule = line.strip().split("|")
        rules_1.append(rule[0].strip())
        rules_2.append(rule[1].strip())

def check_rule(element_index, update):
    pages = update.split(",")
    element = pages[element_index]
    rule_1_indexes = [i for i, x in enumerate(rules_1) if x == element]
    rule_2_indexes = [i for i, x in enumerate(rules_2) if x == element]

    for index in rule_1_indexes:
        second_page = rules_2[index]
        if second_page not in pages:
            continue

        good = False
        for i in range(element_index, len(pages)):
            if pages[i] == second_page:
                good = True
                break

        if not good:
            return False

    for index in rule_2_indexes:
        first_page = rules_1[index]
        if first_page not in pages:
            continue

        good = False
        for i in range(0, element_index):
            if pages[i] == first_page:
                good = True
                break

        if not good:
            return False

    return True

good_updates = []

for update in updates:
    pages = update.split(",")
    good = True

    for i in range(0, len(pages)):
        if not check_rule(i, update):
            good = False
            break

    if good:
        good_updates.append(update)

middle_number_sum = 0
for update in good_updates:
    pages = update.split(",")
    middle_index = len(pages) // 2
    middle_number_sum += int(pages[middle_index])

print(middle_number_sum)