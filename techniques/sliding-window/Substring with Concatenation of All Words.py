def findSubstring(s, words):
    start = [w[0] for w in words]
    result = []
    c = 0
    i = 0
    while i <= len(s) - (len(words) * len(words[0])):
        if s[i] in start:
            o = 0
            while o != len(words[0]) * len(words):
                if s[i + o : i + o + len(words[0])] in words:
                    c += 1
                o += len(words[0])
            if c == len(words):
                result.append(i)
                i += len(words) * len(words[0]) + 1
                c = 0
            else:
                i += 1
        else:
            i += 1
    return result


s = "barfoothefoobarman"
words = ["foo", "bar"]
print(findSubstring(s, words))
# Output: [0,9]

s = "wordgoodgoodgoodbestword"
words = ["word", "good", "best", "word"]
print(findSubstring(s, words))
# Output: []

s = "barfoofoobarthefoobarman"
words = ["bar", "foo", "the"]
print(findSubstring(s, words))
# Output: [6,9,12]
