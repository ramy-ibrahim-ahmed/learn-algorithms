def rotate(nums: list, k: int):
    tmp = nums[len(nums) - k :]
    nums = [*tmp, *nums]
    nums = nums[: len(nums) - k]
    return nums


def rotate(nums: list, k: int):
    n = len(nums)
    k = k % n
    nums[:] = nums[-k:] + nums[:-k]
    return nums


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate(nums=nums, k=k))
# Output: [5,6,7,1,2,3,4]

nums = [-1, -100, 3, 99]
k = 2
print(rotate(nums=nums, k=k))
# Output: [3,99,-1,-100]

nums = [1, 2]
k = 3
print(nums[-3:])  # [2,1]
