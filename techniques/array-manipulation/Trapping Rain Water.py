def trap(height):
    p1 = 0
    p2 = 1
    rain = 0
    curr = 0
    while p2 < len(height):
        # condition start trapping
        if height[p2] < height[p1]:
            curr += height[p1] - height[p2]

        else:
            rain += curr
            p1 = p2
            curr = 0
        p2 += 1

    p1 = len(height) - 1
    p2 = len(height) - 2
    curr = 0

    while p2 >= 0:

        # condition start trapping
        if height[p2] < height[p1]:
            curr += height[p1] - height[p2]

        elif height[p2] == height[p1]:
            p1 = p2

        else:
            rain += curr
            p1 = p2
            curr = 0
        p2 -= 1

    return rain


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height))
# Output: 6

height = [4, 2, 0, 3, 2, 5]
print(trap(height))
# Output: 9
