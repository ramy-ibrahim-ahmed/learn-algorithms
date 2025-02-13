# map_ = {
#     "I": 1,
#     "V": 5,
#     "X": 10,
#     "L": 50,
#     "C": 100,
#     "D": 500,
#     "M": 1000,
# }


def intToRoman(num):
    a = num // 1000
    b = num % 1000 // 100
    c = num % 100 // 10
    d = num % 10
    nums = [a, b, c, d]
    result = []

    for i in range(len(nums)):
        if nums[i] == 0:
            continue
        if i == 0:
            result.append("M" * nums[i])
        elif i == 1:
            result.append(compine(nums[i], "C", "D", "M"))
        elif i == 2:
            result.append(compine(nums[i], "X", "L", "C"))
        elif i == 3:
            result.append(compine(nums[i], "I", "V", "X"))

    return "".join(result)


def compine(num, i, j, k):
    if num == 1:
        return i
    elif num == 4:
        return i + j
    elif num == 5:
        return j
    elif num == 9:
        return i + k
    elif num < 5:
        return i * num
    else:
        return j + (i * (num - 5))


num = 3749
print(intToRoman(num))
# Output: "MMMDCCXLIX"

num = 58
print(intToRoman(num))
# Output: "LVIII"

num = 1994
print(intToRoman(num))
# Output: "MCMXCIV"
