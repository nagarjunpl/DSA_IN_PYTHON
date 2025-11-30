class Solution:
    def quickSort(self, nums):
        n = len(nums)

        if n <= 1:
            return nums

        pivot = nums[n // 2]
        left = [x for x in nums if x < pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]

        return self.quickSort(left) + mid + self.quickSort(right)
