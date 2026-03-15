class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = {')':'(', ']': '[', '}': '{'}

        for char in s:
            if char in check:
                top = stack.pop() if stack else '#'
                if check[char] != top:
                    return False
            else:
                stack.append(char)
        
        return not stack

s = "{[]}"
obj = Solution()
print(obj.isValid(s)) # Output: True
