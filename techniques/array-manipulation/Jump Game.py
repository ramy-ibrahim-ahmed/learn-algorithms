def canJump(nums):
    maxReach = 0
    for i in range(len(nums)):
        if i > maxReach:
            return False
        maxReach = max(maxReach, i + nums[i])
    return True


# nums = [3, 0, 0, 0]
# print(canJump(nums=nums))
# # # Output: True

# nums = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]
# print(canJump(nums=nums))
# # Output: True

# nums = [1, 1, 2, 2, 0, 1, 1]
# print(canJump(nums=nums))
# # Output: True

# nums = [2, 3, 1, 1, 4]
# print(canJump(nums=nums))
# # Output: True

nums = [3, 2, 1, 0, 4]
print(canJump(nums=nums))
# Output: false
