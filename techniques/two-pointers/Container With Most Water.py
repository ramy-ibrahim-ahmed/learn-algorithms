def maxArea(height):
    p1 = 0
    p2 = len(height) - 1
    result = 0
    while p1 < p2:
        curr = min(height[p1], height[p2]) * (p2 - p1)
        result = max(result, curr)
        if height[p1] < height[p2]:
            p1 += 1
        else:
            p2 -= 1
    return result


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))
# Output: 49

height = [1, 1]
print(maxArea(height))
# Output: 1
