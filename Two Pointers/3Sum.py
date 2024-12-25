def threeSum(nums: list):
    nums.sort()
    n = len(nums)
    result = []
    for i in range(1, n - 1):
        p1 = 0
        p2 = n - 1
        while p1 < p2:
            tmp = nums[p1] + nums[p2]
            curr = [nums[p1], nums[i], nums[p2]]
            if tmp > -nums[i]:
                p2 -= 1
            elif tmp < -nums[i]:
                p1 += 1
            elif tmp == -nums[i]:
                if curr not in result:
                    result.append(curr)
                    break
                else:
                    p1 += 1
                    p2 -= 1
    return result


nums = [-2, -1, 0, 0, 0, 1, 2]
print(threeSum(nums))

nums = [3, 0, -2, -1, 1, 2]
print(threeSum(nums))
# Output [[-2,-1,3],[-2,0,2],[-1,0,1]]

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
# Output: [[-1,-1,2],[-1,0,1]]

nums = [0, 0, 0, 0]
print(threeSum(nums))
# Output: [[0, 0, 0]]

nums = [0, 1, 1]
print(threeSum(nums))
# Output: []

nums = [0, 0, 0]
print(threeSum(nums))
# Output: [[0,0,0]]
