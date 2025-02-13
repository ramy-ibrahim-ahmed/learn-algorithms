def candy(ratings):
    n = len(ratings)

    # Step 1: Create an array to store the candies, initialized with 1 candy for each child
    candies = [1] * n

    # Step 2: Left-to-right pass
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Step 3: Right-to-left pass
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    # Step 4: Return the total number of candies
    return sum(candies)


ratings = [1, 3, 2, 2, 1]
print(candy(ratings))
# Output 7

# ratings = [1, 0, 2]
# print(candy(ratings))
# # Output: 5

ratings = [1, 2, 2]
print(candy(ratings))
# Output: 4
