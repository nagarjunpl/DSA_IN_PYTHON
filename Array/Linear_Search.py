class Solution:
    def linearSearch(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            
        return -1

nums = [10, 20, 30, 40, 50]
target = 30
obj = Solution()
print(obj.linearSearch(nums, target)) # Output: 2
