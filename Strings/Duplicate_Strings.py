def printDuplicates(s):
    # Sort the string to group same characters together
    s = ''.join(sorted(s))

    # Traverse the sorted string to count duplicates
    i = 0
    while i < len(s):

        count = 1

        # Count occurrences of current character
        while i + count < len(s) and s[i] == s[i + count]:
            count += 1

        # If count > 1, print the character and its count
        if count > 1:
            print(["" + s[i] + "", count], end=", ")

        # Move to the next different character
        i += count

s = "nagarjun p l"
printDuplicates(s)
