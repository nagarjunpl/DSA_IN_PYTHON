class Solution:
    def floorSqrt(self, n: int) -> int:
        l, r = 0, n
        ans = 0
        while l <= r:
            m = (l + r) // 2
            if m * m <= n:
                ans = m
                l = m + 1
            else:
                r = m - 1
        return ans

n = 50
print(Solution().floorSqrt(n)) #Output : 7
