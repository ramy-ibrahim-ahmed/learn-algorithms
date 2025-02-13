def removeDuplicates(nums):
    if len(nums) <= 2:
        return len(nums)

    i = 2

    for j in range(2, len(nums)):
        if nums[j] != nums[i - 2]:
            nums[i] = nums[j]
            i += 1

    return i


nums = [1, 1, 1, 2, 2, 3]
print(removeDuplicates(nums=nums))
# Output: 5, nums = [1,1,2,2,3,_]

nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(removeDuplicates(nums=nums))
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
