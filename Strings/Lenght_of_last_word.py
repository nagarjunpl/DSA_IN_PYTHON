class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new = s.strip().split()
        rev = new[::-1]
        for j in rev[0:2]:
            return len(j)

s = "Hello World"
obj = Solution()
print(obj.lengthOfLastWord(s)) # Output: 5
