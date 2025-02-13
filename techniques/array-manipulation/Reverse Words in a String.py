def reverseWords(s):
    result = ""
    curr = ""
    for c in s:
        if c != " ":
            curr = curr + c
        elif c == " " and curr and result == "":
            result = curr + result
            curr = ""
        elif c == " " and curr and result:
            result = curr + " " + result
            curr = ""
    if not result:
        result = curr
        curr = ""
    return curr + " " + result if curr else result


s = "EPY2giL"
print(reverseWords(s))
# Output: "EPY2giL"

s = "the sky is blue"
print(reverseWords(s))
# Output: "blue is sky the"

s = "  hello world  "
print(reverseWords(s))
# Output: "world hello"

s = "a good   example"
print(reverseWords(s))
# Output: "example good a"
