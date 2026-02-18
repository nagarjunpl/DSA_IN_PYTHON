class Solution:
    def largestElement(self, nums):
        largest = nums[0]

        for num in nums:
            if largest < num:
                largest = num

        return largest

s = Solution()
print(s.largestElement([4,3,5,8,1]))
