class Solution:
    def findKRotation(self, nums):
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return l 

nums = [4, 5, 1, 2]
print(Solution().findKRotation(nums)) # Output : 2
