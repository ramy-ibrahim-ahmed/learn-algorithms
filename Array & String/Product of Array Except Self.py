def productExceptSelf(nums):
    n = len(nums)

    # Create an output array initialized to 1
    # [1, 1, 1, 1]
    result = [1] * n

    # Pass 1: Calculate the prefix products
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i] 

    # Pass 2: Calculate the suffix products and multiply them with the result
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


nums = [1, 2, 3, 4]
print(productExceptSelf(nums))
# Output: [24,12,8,6]

nums = [-1, 1, 0, -3, 3]
print(productExceptSelf(nums))
# Output: [0,0,9,0,0]
