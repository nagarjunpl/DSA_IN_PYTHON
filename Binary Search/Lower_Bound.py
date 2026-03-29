class Solution:
    def lowerBound(self, nums, x):
        if nums[0] >= x:
            return 0

        if nums[-1] < x:
            return len(nums)

        for i in range(len(nums) - 1):
            if nums[i] < x and nums[i + 1] >= x:
                return i + 1

nums = [3, 5, 8, 15, 19]  
x = 3

obj = Solution()
print(obj.lowerBound(nums, x)) # Output : 0
