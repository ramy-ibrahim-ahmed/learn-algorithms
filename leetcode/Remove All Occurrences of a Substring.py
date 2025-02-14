# condition for put p1 on first
# if yes go furthur till reach end on best case del from p1 to p2
# if not p2 ++
def removeOccurrences(s: str, part: str):
    while part in s:
        s = s.replace(part, "", 1)
    return s


s = "daabcbaabcbc"
part = "abc"
print(removeOccurrences(s, part))
# Output: "dab"

s = "axxxxyyyyb"
part = "xy"
print(removeOccurrences(s, part))
# Output: "ab"
