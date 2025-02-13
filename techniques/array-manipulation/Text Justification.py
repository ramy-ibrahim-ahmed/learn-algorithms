def fullJustify(words, maxWidth):
    result = []
    curr = []
    quota = maxWidth
    for w in words:
        if len(w) <= quota and len(w) <= quota - len(curr):
            curr.append(w)
            quota = quota - len(w)
        else:
            if quota % (len(curr) - 1) == 0:
                spaces = quota // (len(curr) - 1) * " "
                row = spaces.join(curr)
                result.append(row)
            else:
                spaces = ((quota // (len(curr) - 1)) + 1) * " "
                row = spaces.join(curr[:-1])
                row = row + " " + curr[-1]
                result.append(row)
            curr = [w]
            quota = maxWidth - len(w)
    last_row = " ".join(curr)
    last_row_spaces = quota
    last_row = last_row + last_row_spaces * " "
    result.append(last_row)
    return result


#########################################################################################################################
def fullJustify(words, maxWidth):
    result = []
    current_line = []
    num_of_letters = 0

    for word in words:
        # Check if adding the new word exceeds maxWidth
        if num_of_letters + len(word) + len(current_line) > maxWidth:
            # Time to justify the current line
            if len(current_line) == 1:
                # Special case: if only one word is in the line
                result.append(current_line[0] + " " * (maxWidth - num_of_letters))
            else:
                # Distribute spaces
                total_spaces = maxWidth - num_of_letters
                space_between_words = total_spaces // (len(current_line) - 1)
                extra_spaces = total_spaces % (len(current_line) - 1)

                for i in range(extra_spaces):
                    current_line[i] += " "

                line = (" " * space_between_words).join(current_line)
                result.append(line)

            # Reset for the new line
            current_line = []
            num_of_letters = 0

        # Add the current word to the line
        current_line.append(word)
        num_of_letters += len(word)

    # Last line handling: left-justified
    last_line = " ".join(current_line)
    last_line += " " * (maxWidth - len(last_line))
    result.append(last_line)

    return result


# Test cases
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
print(fullJustify(words, maxWidth))
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]

words = ["What", "must", "be", "acknowledgment", "shall", "be"]
maxWidth = 16
print(fullJustify(words, maxWidth))
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]

words = [
    "Science",
    "is",
    "what",
    "we",
    "understand",
    "well",
    "enough",
    "to",
    "explain",
    "to",
    "a",
    "computer.",
    "Art",
    "is",
    "everything",
    "else",
    "we",
    "do",
]
maxWidth = 20
print(fullJustify(words, maxWidth))
# Output:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]
