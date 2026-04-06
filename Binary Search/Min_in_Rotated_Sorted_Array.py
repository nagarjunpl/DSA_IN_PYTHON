class Solution:
    def findMin(self, nums):
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]

nums = [4, 5, 6, 7, -7, 1, 2, 3]
print(Solution().findMin(nums)) #Output : -7
