#!/usr/bin/python3
def uniq_add(my_list=[]):
    nums = []
    for i in my_list:
        if i not in nums:
            nums.append(i)
    return sum(nums)
