def minimizeXor(num1, num2):
    target_set_bits = bin(num2).count("1")
    current_set_bits = bin(num1).count("1")
    x = num1

    # If num1 already has the correct number of set bits
    if current_set_bits == target_set_bits:
        return x

    # 32-bit representation
    bits = list(bin(num1)[2:].zfill(32))

    if current_set_bits > target_set_bits:
        # Turn off extra bits (1 -> 0) from the least significant bit (LSB)
        for i in range(len(bits) - 1, -1, -1):
            if bits[i] == "1":
                bits[i] = "0"
                current_set_bits -= 1
                if current_set_bits == target_set_bits:
                    break
    else:
        # Turn on more bits (0 -> 1) from the least significant bit (LSB)
        for i in range(len(bits) - 1, -1, -1):
            if bits[i] == "0":
                bits[i] = "1"
                current_set_bits += 1
                if current_set_bits == target_set_bits:
                    break

    # Convert back to integer and return
    return int("".join(bits), 2)


num1 = 3
num2 = 5
print(minimizeXor(num1, num2))  # Output: 3

num1 = 1
# 0 0 0 0 0 .... 0 0 0 1
num2 = 12
# 0 0 0 0 0 .... 1 0 1 0
print(minimizeXor(num1, num2))  # Output: 3
