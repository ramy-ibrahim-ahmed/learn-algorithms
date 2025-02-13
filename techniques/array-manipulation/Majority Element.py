def majorityElement(nums: list):
    counts = dict()
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    return max(counts, key=counts.get)


from collections import Counter


def majorityElement(nums: list):
    counts = Counter(nums)
    return max(counts, key=counts.get)


nums = [3, 2, 3]
print(majorityElement(nums=nums))
# Output: 3

nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums=nums))
# Output: 2
