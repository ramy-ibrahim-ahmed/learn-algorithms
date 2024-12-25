# 1. get a b c till notice a in the dict the by a index slice and sart again.
def lengthOfLongestSubstring(s):
    n = len(s)
    maxLength = 0
    charSet = set()
    p1 = 0

    for p2 in range(n):
        while s[p2] in charSet:
            charSet.remove(s[p1])
            p1 += 1
        charSet.add(s[p2])
        maxLength = max(maxLength, p2 - p1 + 1)

    return maxLength


s = "abcabcbb"
print(lengthOfLongestSubstring(s))
# Output: 3

# s = "bbbbb"
# print(lengthOfLongestSubstring(s))
# # Output: 1

s = "pwwkew"
print(lengthOfLongestSubstring(s))
# Output: 3
