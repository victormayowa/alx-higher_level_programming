#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_nums = []
    sum = 0
    for num in my_list:
        if num not in unique_nums:
            sum += num
            unique_nums.append(num)
    return sum

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
