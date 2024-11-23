def sum_of_list(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum_of_list(lst[1:])

numbers = [3, 1, 4, 1, 5, 9]
print(f"The sum of the list {numbers} is {sum_of_list(numbers)}")
