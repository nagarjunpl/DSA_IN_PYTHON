# Palindrome Checker Using Recursion

class Solution:    
    def palindromeCheck(self, s: str) -> bool:
        def helper(left, right):
            if left >= right:
                return True
                
            if s[left] != s[right]:
                return False
                
            return helper(left + 1, right - 1)
        
        return helper(0, len(s) - 1)

a = Solution()
print(a.palindromeCheck("nameman"))  # True
print(a.palindromeCheck("cornonrc"))  # False
