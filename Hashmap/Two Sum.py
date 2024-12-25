def twoSum(nums, target):
    n = len(nums)
    hashmap = dict()
    for i in range(n):
        if target - nums[i] in hashmap:
            return [hashmap[target - nums[i]], i]
        else:
            hashmap[nums[i]] = i
    return []


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))
# Output: [0,1]

nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))
# Output: [1,2]

nums = [3, 3]
target = 6
print(twoSum(nums, target))
# Output: [0,1]
