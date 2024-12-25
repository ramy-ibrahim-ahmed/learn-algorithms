def isPalindrome(s: str):
    s = s.lower()
    n = len(s)
    p1 = 0
    p2 = n - 1
    while p1 < p2:
        if not s[p1].isalnum():
            p1 += 1
            continue
        elif not s[p2].isalnum():
            p2 -= 1
            continue
        elif s[p1] != s[p2]:
            return False
        else:
            p1 += 1
            p2 -= 1
    return True


s = ",,,,,,,,,,,,acva"
print(isPalindrome(s))
# Output: false

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
# Output: true

s = "race a car"
print(isPalindrome(s))
# Output: false

s = " "
print(isPalindrome(s))
# Output: true
