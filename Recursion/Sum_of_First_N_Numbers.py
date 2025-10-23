class Solution:
    def NnumbersSum(self, n):
        if n == 0:
            return 0
            
        return n + self.NnumbersSum(n - 1)

a = Solution()
print(a.NnumbersSum(5)) # OUTPUT : 15
print(a.NnumbersSum(8)) # OUTPUT : 36
