def xorAllNums(nums1, nums2):
    xor1 = 0
    xor2 = 0
    for num1 in nums1:
        for num2 in nums2:
            xor1 = num1 ^ num2
            xor2 = xor2 ^ xor1
    return xor2


def xorAllNums(nums1, nums2):
    m1 = len(nums1)
    m2 = len(nums2)
    # Case 1: Both lengths are even
    if m1 % 2 == 0 and m2 % 2 == 0:
        return 0
    # Case 2: nums2 has even length, nums1 has odd length
    elif m1 % 2 == 0:
        xor1 = 0
        for num in nums1:
            xor1 ^= num
        return xor1
    # Case 3: nums1 has even length, nums2 has odd length
    elif m2 % 2 == 0:
        xor2 = 0
        for num in nums2:
            xor2 ^= num
        return xor2
    # Case 4: Both lengths are odd
    else:
        xor1 = 0
        xor2 = 0
        for num in nums1:
            xor1 ^= num
        for num in nums2:
            xor2 ^= num
        return xor1 ^ xor2


# Test cases
nums1 = [2, 1, 3]
nums2 = [10, 2, 5, 0]
print(xorAllNums(nums1, nums2))  # Expected Output: 13

nums1 = [1, 2]
nums2 = [3, 4]
print(xorAllNums(nums1, nums2))  # Expected Output: 0
