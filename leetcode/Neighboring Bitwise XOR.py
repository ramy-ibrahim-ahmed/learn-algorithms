def doesValidArrayExist(derived):
    n = len(derived)

    # Function to validate the circular condition
    def is_valid(start_value):
        original = [0] * n
        original[0] = start_value

        # Reconstruct the array based on XOR rules
        for i in range(1, n):
            original[i] = derived[i - 1] ^ original[i - 1]

        # Check the circular condition
        return original[n - 1] ^ original[0] == derived[n - 1]

    # Check for both possible starting values (0 or 1)
    return is_valid(0) or is_valid(1)


derived = [1, 1, 0]
print(doesValidArrayExist(derived))
# Output: true


derived = [1, 1]
print(doesValidArrayExist(derived))
# Output: true

derived = [0, 0]
print(doesValidArrayExist(derived))
# Output: true

derived = [1, 0]
print(doesValidArrayExist(derived))
# Output: false
