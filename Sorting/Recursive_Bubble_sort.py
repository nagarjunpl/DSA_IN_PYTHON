class Solution:
    def bubbleSort(self, nums):
        def sort_rec(nums, n):
            if n == 1:
                return

            for i in range(n-1):
                if nums[i] > nums[i+1]:
                    nums[i+1], nums[i] = nums[i], nums[i+1]

            sort_rec(nums, n-1)

        sort_rec(nums, len(nums))
        return nums
