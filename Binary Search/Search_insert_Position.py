class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
            break

        elif nums[0] > target:
            return 0

        elif nums[-1] < target:
            return len(nums)
            
        for i in range(len(nums) - 1):
            if nums[i] < target and nums[i+1] > target:
                return i + 1

nums = [1, 3, 5, 6]
target = 7
obj = Solution()
print(obj.searchInsert(nums, target)) # output : 4
