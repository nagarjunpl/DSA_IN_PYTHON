class Solution:    
    def palindromeCheck(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

a = Solution()
print(a.palindromeCheck("aruura")) # OUTPUT : True
print(a.palindromeCheck("sbipbs")) # OUTPUT : False
