def isIsomorphic(s, t):
    hashmap = dict()

    for i in range(len(s)):
        if s[i] not in hashmap:

            if t[i] in hashmap.values():
                return False

            hashmap[s[i]] = t[i]

        else:
            if hashmap[s[i]] != t[i]:
                return False

    return True


s = "badc"
t = "baba"
print(isIsomorphic(s, t))
# Expected false

s = "egg"
t = "add"
print(isIsomorphic(s, t))
# Output: true

s = "foo"
t = "bar"
print(isIsomorphic(s, t))
# Output: false


s = "paper"
t = "title"
print(isIsomorphic(s, t))
# Output: true
