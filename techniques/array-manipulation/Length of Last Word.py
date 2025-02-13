def lengthOfLastWord(s):
    result = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == " " and result > 0:
            return result
        elif s[i] != " ":
            result += 1
    return result


s = "Hello World"
print(lengthOfLastWord(s))
# Output: 5

s = "   fly me   to   the moon  "
print(lengthOfLastWord(s))
# Output: 4

s = "luffy is still joyboy"
print(lengthOfLastWord(s))
# Output: 6
