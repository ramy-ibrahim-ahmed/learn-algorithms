# [0, 1, 2, 2, 3, 0, 4, 2]
# 1. pointer -> till find val
# 2. pop val
# 3. push add _ at end
# 4. stay at same place till num != val
def removeElement(nums: list, val: int):
    n = len(nums)
    left_pointer = 0
    num_ = 0
    iter = 0
    while iter < n:
        if nums[left_pointer] == val:
            nums.pop(left_pointer)
            nums.append("_")
            num_ += 1
        else:
            left_pointer += 1
        iter += 1
    return n - num_, nums


nums = [3, 2, 2, 3]
val = 3
print(removeElement(nums=nums, val=val))
# Output: 2, nums = [2,2,_,_]

nums = [0,1,2,2,3,0,4,2]
val = 3
print(removeElement(nums=nums, val=val))
# Output: 5, nums = [0,1,4,0,3,_,_,_]
