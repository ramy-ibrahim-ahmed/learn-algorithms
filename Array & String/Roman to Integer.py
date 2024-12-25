def romanToInt(s):
    result = 0
    map_ = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    for c in range(len(s) - 1):
        if map_[s[c]] >= map_[s[c + 1]]:
            result += map_[s[c]]
        else:
            result -= map_[s[c]]
    return result + map_[s[-1]]


s = "MCMXCIV"
print(romanToInt(s))
# Output: 1994

# s = "III"
# print(romanToInt(s))
# # Output: 3

# s = "LVIII"
# print(romanToInt(s))
# # Output: 58
