def number_occurence(target_number, sorted_num_list) -> int:
    occurence = 0
    index = 0
    max_index = len(sorted_num_list) - 1

    while not sorted_num_list[index] > target_number:
        if sorted_num_list[index] == target_number:
            occurence += 1
        
        index += 1

        if index > max_index:
            break

    return occurence

with open('/workspaces/aoc24/day01/lists.txt') as f:
    lines = f.readlines()
    first_list = []
    second_list = []

    for line in lines:
        line = line.strip()
        if line:
            entry_pair = line.split()
            first_list.append(int(entry_pair[0]))
            second_list.append(int(entry_pair[1]))

    assert len(first_list) == len(second_list)

    first_list.sort()
    second_list.sort()

    distance_sum = 0
    similarity_score = 0

    for i in range(len(first_list)):
        first_number = first_list[i]
        second_number = second_list[i]

        distance_sum += abs(first_number - second_number)
        similarity_score += first_number * number_occurence(first_number, second_list)

    print(f"Sum of distances is {distance_sum}")
    print(f"Similarity score is {similarity_score}")

    exit()