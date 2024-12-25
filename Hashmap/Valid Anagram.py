def isAnagram(s, t):
    n = len(s)
    m = len(t)

    if n != m:
        return False

    hashmap = dict()
    for i in range(n):
        if s[i] not in hashmap:
            hashmap[s[i]] = 1
        elif s[i] in hashmap:
            hashmap[s[i]] += 1
            if hashmap[s[i]] == 0:
                del hashmap[s[i]]

        if t[i] not in hashmap:
            hashmap[t[i]] = -1
        elif t[i] in hashmap:
            hashmap[t[i]] -= 1
            if hashmap[t[i]] == 0:
                del hashmap[t[i]]

    return True if len(hashmap) == 0 else False


s = "anagram"
t = "nagaram"
print(isAnagram(s, t))
# Output: true


s = "rat"
t = "car"
print(isAnagram(s, t))
# Output: false
