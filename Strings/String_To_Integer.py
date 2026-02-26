class Solution:
    def st_int(self, input):
        i = 0
        n = len(input)
        num = 0

        while i < n and input[i] == ' ':
            i += 1
            
        while i < n and input[i].isdigit():
            num = num * 10 + int(input[i])
            i += 1

        return num

s = input("Enter a string: ")  # Enter a string: 4193 with words
sol = Solution()
result = sol.st_int(s)
print("Converted Integer:", result)  # Converted Integer: 4193
