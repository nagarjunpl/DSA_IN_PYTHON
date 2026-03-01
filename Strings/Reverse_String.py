def reverseString(s):
    rvs = []
    for char in s:
        rvs.append(char)
    return "".join(rvs[::-1])

s = "Python"
result = reverseString(s)
print("Output:", result)  # Output: nohtyP
