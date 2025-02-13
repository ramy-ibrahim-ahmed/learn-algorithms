def convert(s, numRows):
    if numRows == 1:
        return s

    rows = [""] * numRows
    curr_row = 0
    going_down = False
    for c in s:
        rows[curr_row] += c
        if curr_row == 0 or curr_row == numRows - 1:
            going_down = not going_down
        curr_row += 1 if going_down else -1

    return "".join(rows)


s = "PAYPALISHIRING"
numRows = 3
print(convert(s, numRows))
# P   A   H   N
# A P L S I I G
# Y   I   R
# Output: "PAHNAPLSIIGYIR"

s = "PAYPALISHIRING"
numRows = 4
print(convert(s, numRows))
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Output: "PINALSIGYAHRPI"

s = "A"
numRows = 1
print(convert(s, numRows))
# Output: "A"
