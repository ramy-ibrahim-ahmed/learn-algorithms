def wordPattern(pattern: str, s: str):
    words = s.split()

    n = len(words)
    m = len(pattern)
    if n != m:
        return False

    hashmap = dict()
    for i in range(m):
        if pattern[i] not in hashmap:

            if words[i] in hashmap.values():
                return False

            hashmap[pattern[i]] = words[i]

        elif hashmap[pattern[i]] != words[i]:
            return False
    return True


pattern = "abba"
s = "dog dog dog dog"
print(wordPattern(pattern, s))
# Expected false


pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern, s))
# Output: true

pattern = "abba"
s = "dog cat cat fish"
print(wordPattern(pattern, s))
# Output: false

pattern = "aaaa"
s = "dog cat cat dog"
print(wordPattern(pattern, s))
# Output: false
