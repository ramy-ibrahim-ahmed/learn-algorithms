def longestCommonPrefix(strs):
    perfix = strs[0]
    for i in range(1, len(strs)):
        if len(strs[i] == 0):
            return ""

        j = 0
        while j < len(perfix) and j < len(strs[i]):
            if strs[i][j] != perfix[j]:
                perfix = perfix[:j]
                break
            elif j == len(strs[i]) - 1:
                perfix = perfix[: j + 1]
            j += 1
    return perfix


strs = ["ab", "a"]
print(longestCommonPrefix(strs))
# Output: "fl"

strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))
# Output: "fl"

strs = ["dog", "racecar", "car"]
print(longestCommonPrefix(strs))
# Output: ""
