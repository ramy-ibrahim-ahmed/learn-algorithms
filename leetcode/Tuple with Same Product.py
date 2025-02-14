def tupleSameProduct(nums):
    n = len(nums)
    hash_table = dict()

    for i in range(n):
        for j in range(i + 1, n):
            product = nums[i] * nums[j]
            if product not in hash_table:
                hash_table[product] = 1
            else:
                hash_table[product] += 1

    result = 0

    for count in hash_table.values():
        if count >= 2:
            result += count * (count - 1) * 4

    return result


nums = [2, 3, 4, 6]
print(tupleSameProduct(nums))
# Output: 8

nums = [1, 2, 4, 5, 10]
print(tupleSameProduct(nums))
# Output: 16

nums = [2, 3, 4, 6, 8, 12]
print(tupleSameProduct(nums))
# Output: 40
