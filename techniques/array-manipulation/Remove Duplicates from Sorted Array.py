def removeDuplicates(nums: list):
    m = len(nums)
    redundant = 0
    pointer1 = 0
    pointer2 = 1
    i = 0
    while i < m and pointer2 < m:
        if nums[pointer1] == nums[pointer2]:
            nums.pop(nums[pointer2])
            nums.append("_")
            redundant += 1
        else:
            pointer1 += 1
            pointer2 += 1
        i += 1
    return m - redundant, nums


nums = [-1,0,0,0,0,3,3]
print(removeDuplicates(nums=nums))
# Output: 2, nums = [1,2,_]


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(nums=nums))
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
