class Solution:
    def reverse(self, arr: list, n: int) -> None:
        left = 0
        right = n - 1
        
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        
        return arr


a = Solution()
print(a.reverse([1, 2, 3, 3, 6, 7], 6))   # Output: [7, 6, 3, 3, 2, 1]
