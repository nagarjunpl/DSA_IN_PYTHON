class Solution:
    def removeDuplicates(self, nums):
        count=1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[count] = nums[i]
                count += 1
        
        return count

nums = [-30, -30, 0, 0, 10, 20, 30, 30]
k = Solution()
print("Number of unique elements:", k.removeDuplicates(nums))
