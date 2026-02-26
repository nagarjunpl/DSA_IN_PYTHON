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
