class Solution:
    def moveZeroes(self, nums):
        j = 0  

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1

        print(nums)

nums = [0,1,0,3,12]
sol = Solution()
sol.moveZeroes(nums) # Output : [1, 3, 12, 0, 0]
