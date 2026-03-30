class Solution:
    def upperBound(self, nums, x):
        if nums[0] > x:
            return 0

        if nums[-1] <= x:
            return len(nums)

        for i in range(len(nums) - 1):
            if nums[i] <= x and nums[i + 1] > x:
                return i + 1

nums = [1, 2, 2, 3]
x = 2
obj = Solution()
print(obj.upperBound(nums, x)) # Output : 3
