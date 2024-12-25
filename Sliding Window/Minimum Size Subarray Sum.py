def minSubArrayLen(target: int, nums: list):
    n = len(nums)
    p1 = 0
    result = float("inf")
    currunt_sum = 0

    for p2 in range(n):
        currunt_sum += nums[p2]

        while currunt_sum >= target:
            result = min(result, p2 - p1 + 1)
            currunt_sum -= nums[p1]
            p1 += 1

    return result if result != float("inf") else 0


target = 11
nums = [1, 2, 3, 4, 5]
print(minSubArrayLen(target, nums))
# Output 3

target = 7
nums = [2, 3, 1, 2, 4, 3]
print(minSubArrayLen(target, nums))
# Output: 2

target = 4
nums = [1, 4, 4]
print(minSubArrayLen(target, nums))
# Output: 1

target = 11
nums = [1, 1, 1, 1, 1, 1, 1, 1]
print(minSubArrayLen(target, nums))
# Output: 0
