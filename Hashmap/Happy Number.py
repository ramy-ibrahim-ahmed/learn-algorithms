def isHappy(n: int) -> bool:
    def sum_of_squares(num: int) -> int:
        return sum(int(digit) ** 2 for digit in str(num))

    seen = set()
    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        n = sum_of_squares(n)
    return True


n = 19
print(isHappy(n))
# Output: true

n = 2
print(isHappy(n))
# Output: false
