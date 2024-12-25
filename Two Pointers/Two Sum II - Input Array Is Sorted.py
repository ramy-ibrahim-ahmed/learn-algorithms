def twoSum(numbers, target):
    n = len(numbers)
    p1 = 0
    p2 = n - 1
    while p1 < p2:
        if numbers[p1] + numbers[p2] < target:
            p1 += 1
        elif numbers[p1] + numbers[p2] > target:
            p2 -= 1
        else:
            return [p1 + 1, p2 + 1]


numbers = [2, 7, 11, 15]
target = 9
print(twoSum(numbers, target))
# Output: [1,2]

numbers = [2, 3, 4]
target = 6
print(twoSum(numbers, target))
# Output: [1,3]

numbers = [-1, 0]
target = -1
print(twoSum(numbers, target))
# Output: [1,2]
