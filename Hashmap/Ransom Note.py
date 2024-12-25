def canConstruct(ransomNote, magazine):
    charmap = {}
    for char in ransomNote:
        if char not in charmap:
            charmap[char] = 1
        else:
            charmap[char] += 1

    for char in magazine:
        if char in charmap:
            charmap[char] -= 1

            if charmap[char] == 0:
                del charmap[char]

    return True if len(charmap) == 0 else False


ransomNote = "a"
magazine = "b"
print(canConstruct(ransomNote, magazine))
# Output: false

ransomNote = "aa"
magazine = "ab"
print(canConstruct(ransomNote, magazine))
# Output: false

ransomNote = "aa"
magazine = "aab"
print(canConstruct(ransomNote, magazine))
# Output: true
