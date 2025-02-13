def jump(nums):
    n = len(nums)
    if n == 1:
        return 0

    jumps = 0
    currentEnd = 0
    maxReach = 0
    for i in range(n - 1):
        # Update the farthest we can reach from index i
        maxReach = max(maxReach, i + nums[i])

        # If we have reached the end of the range of the current jump
        if i == currentEnd:
            jumps += 1
            currentEnd = maxReach

            # If we've reached or passed the last index, break out of the loop
            if currentEnd >= n - 1:
                break
    return jumps


nums = [1, 2, 4, 1, 1, 1, 1, 1]
print(jump(nums=nums))
# Output: 0

nums = [2, 3, 1, 1, 4]
print(jump(nums=nums))
# Output: 2

nums = [2, 3, 0, 1, 4]
print(jump(nums=nums))
# Output: 2
