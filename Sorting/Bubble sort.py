class Solution:
    def bubbleSort(self, nums):
        n = len(nums)
        
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        print(nums)
        
# Example usage
sol = Solution()
sol.bubbleSort([64, 34, 25, 12, 22, 11, 90])



