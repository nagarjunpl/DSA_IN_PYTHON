class Solution:
    def singleNonDuplicate(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if m % 2 == 1:
                m -= 1
            if nums[m] == nums[m + 1]:
                l = m + 2
            else:
                r = m
        return nums[l]

nums = [1,1,2,2,3,3,4,4,5,5,6,6,7]
print(Solution().singleNonDuplicate(nums)) #Output: 7
