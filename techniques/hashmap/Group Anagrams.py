def groupAnagrams(strs: str):
    hashmap = dict()
    result = []
    for word in strs:
        chars = [c for c in word]
        chars.sort()
        chars = "".join(chars)
        if chars not in hashmap:
            hashmap[chars] = len(result)
            result.append([word])
        else:
            result[hashmap[chars]].append(word)
    return result


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

strs = [""]
print(groupAnagrams(strs))
# Output: [[""]]

strs = ["a"]
print(groupAnagrams(strs))
# Output: [["a"]]
