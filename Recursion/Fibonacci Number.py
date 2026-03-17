class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        return self.fib(n - 1) + self.fib(n - 2)

a = Solution()
print(a.fib(2))   # Output: 1
print(a.fib(3))   # Output: 2
print(a.fib(6))   # Output: 8



# Better Approach
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
            
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
        
a = Solution()
print(a.fib(6))   #Output : 8
