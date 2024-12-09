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

bad_updates = []

for update in updates:
    pages = update.split(",")
    good = True

    for i in range(0, len(pages)):
        if not check_rule(i, update):
            good = False
            break

    if not good:
        bad_updates.append(update)


def fix_update(element_index, update):
    pages = update.split(",")
    element = pages[element_index]
    rule_1_indexes = [i for i, x in enumerate(rules_1) if x == element]
    rule_2_indexes = [i for i, x in enumerate(rules_2) if x == element]

    for index in rule_1_indexes:
        second_page = rules_2[index]
        if second_page not in pages:
            continue

        for i in range(0, element_index):
            if pages[i] == second_page:
                pages[i], pages[element_index] = pages[element_index], pages[i]
                break

    for index in rule_2_indexes:
        first_page = rules_1[index]
        if first_page not in pages:
            continue

        for i in range(element_index, len(pages)):
            if pages[i] == first_page:
                pages[i], pages[element_index] = pages[element_index], pages[i]
                break

    update = ",".join(pages)
    return update

fixed_updates = []
for update in bad_updates:
    pages = update.split(",")
    applied_rules_1_indexes = [i for i, x in enumerate(rules_1) if x in pages]
    applied_rules_2_indexes = [i for i, x in enumerate(rules_2) if x in pages]
    new_update = update

    good = False
    while not good:
        for i in range(len(pages)):
            new_update = fix_update(i, new_update)
            good = True
            for j in range(0, len(pages)):
                if not check_rule(j, new_update):
                    good = False
                    break

    fixed_updates.append(new_update)

print(bad_updates[0])
print(fixed_updates[0])

fixed_middle_number_sum = 0
for update in fixed_updates:
    pages = update.split(",")
    middle_index = len(pages) // 2
    middle_number = int(pages[middle_index])
    fixed_middle_number_sum += middle_number

print(fixed_middle_number_sum)