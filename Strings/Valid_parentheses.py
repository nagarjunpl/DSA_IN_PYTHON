class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = {')':'(', ']': '[', '}': '{'}

        for char in s:
            if char in check:  # if it is a closing bracket
                top = stack.pop() if stack else '#'  # get top of stack
                if check[char] != top:
                    return False
            else:
                stack.append(char)  # push opening bracket
        
        return not stack  # valid if stack is empty
