def reverseString(s):
    # Initialize an empty string to store the reversed result
    rvs = ""
    
    # Loop through each character in the input string
    for char in s:
        # Add the current character in front of the existing reversed string
        rvs = char + rvs
    
    # Return the final reversed string
    return rvs
