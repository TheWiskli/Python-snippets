def count_Occurrences(numbers):
    occurrences = {}

    for number in numbers:
        if number in occurrences:
            occurrences[number] += 1
        else:
            occurrences[number] = 1
    return occurrences

numbers_List = [7,11,1,10,3,9,8,9,9,11,4,11,2,9,3,5,2,5,1,3,2,8,1,5,1,5,4,7,5,6,2,3,7,9,3,12,2,7,3,8,1,9,2,9,3,6,9,12,1,10,6,12,2,12,1,10,2,6,10,11]
numbers_List.sort()
result = count_Occurrences(numbers_List)

print("Number Occurrenses:")
for number, count in result.items():
    print(f"{number}: {count} times.")