def isSubsequence(s, t):
    n = len(t)
    m = len(s)
    p1 = 0
    p2 = 0

    if m == 0:
        return True

    while p2 < n:
        if s[p1] == t[p2]:
            p1 += 1
            p2 += 1
            if p1 == m:
                return True
        else:
            p2 += 1
    return False


s = "bb"
t = "ahbgdc"
print(isSubsequence(s, t))
# Output: false


s = "abc"
t = "ahbgdc"
print(isSubsequence(s, t))
# Output: true

s = "axc"
t = "ahbgdc"
print(isSubsequence(s, t))
# Output: false
