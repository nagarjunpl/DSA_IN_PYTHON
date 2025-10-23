
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        return self.fib(n - 1) + self.fib(n - 2)


a = Solution()
print(a.fib(2))   # Output: 1
print(a.fib(3))   # Output: 2
print(a.fib(6))   # Output: 8
