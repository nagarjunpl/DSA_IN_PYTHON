class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

nums = [3,2,4]
target = 6
obj = Solution()
print(obj.twoSum(nums, target)) # Output : [1,2]
