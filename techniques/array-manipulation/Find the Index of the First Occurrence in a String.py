def strStr(haystack, needle):
    n = len(haystack)
    m = len(needle)

    if m == 0:
        return 0

    for i in range(n - m + 1):
        if haystack[i : i + m] == needle:
            return i

    return -1


haystack = "mississippi"
needle = "issip"
print(strStr(haystack, needle))
# Output: 4

haystack = "a"
needle = "a"
print(strStr(haystack, needle))
# Output: 0

haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack, needle))
# Output: 0


haystack = "leetcode"
needle = "leeto"
print(strStr(haystack, needle))
# Output: -1
