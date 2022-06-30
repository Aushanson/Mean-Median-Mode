def mode(num_list):
    max_count = (0, 0)
    for num in num_list:
        occurrences = num_list.count(num)
        if occurrences > max_count[0]:
            max_count = (occurrences, num)
    return max_count[1]


def median(num_list):
    num_list.sort()
    if len(num_list) % 2 != 0:
        middle_num = int((len(num_list) - 1) / 2)
        return num_list[middle_num]
    elif len(num_list) % 2 == 0:
        middle_num_1 = int(len(num_list) / 2)
        middle_num_2 = int(len(num_list) / 2) - 1
        return mean([num_list[middle_num_1], num_list[middle_num_2]])


num_list = [int(x) for x in input("Enter a list of numbers: ").split()]
print(num_list)
print("Mean:", mean(num_list))
print("Median:", median(num_list))
print("Mode:", mode(num_list))
