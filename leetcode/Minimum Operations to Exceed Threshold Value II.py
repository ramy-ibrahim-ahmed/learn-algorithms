# def minOperations(nums: list, k: int):
#     operations = 0
#     while len(nums) >= 2:
#         if min(nums) >= k:
#             break
#         min1 = min(nums)
#         nums.remove(min1)
#         min2 = min(nums)
#         nums.remove(min2)
#         nums.append((min1 * 2) + min2)
#         operations += 1
#     return operations

import heapq


def minOperations(nums: list, k: int):
    operations = 0
    heapq.heapify(nums)

    while len(nums) >= 2 and nums[0] < k:
        min1 = heapq.heappop(nums)
        min2 = heapq.heappop(nums)
        heapq.heappush(nums, (min1 * 2) + min2)
        operations += 1
    return operations


nums = [2, 11, 10, 1, 3]
k = 10
print(minOperations(nums, k))
# Output: 2

nums = [1, 1, 2, 4, 9]
k = 20
print(minOperations(nums, k))
# Output: 4
