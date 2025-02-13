"""_thoughts_

- sort the array.
- iterate throw papers and condition adding h index
"""


def hIndex(citations: list):
    m = len(citations)
    citations.sort(reverse=True)
    h = 0
    for i in range(m):
        if i + 1 > citations[i]:
            break
        else:
            h += 1
    return h


citations = [3, 0, 6, 1, 5]
print(hIndex(citations))
# Output: 3

citations = [1]
print(hIndex(citations))
# Output: 1

citations = [1, 3, 1]
print(hIndex(citations))
# Output: 1
