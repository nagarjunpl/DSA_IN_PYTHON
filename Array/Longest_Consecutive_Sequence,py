class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        nums = sorted(set(nums))
        longest = 1
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                count += 1
                longest = max(longest, count)
            else:
                count = 1
        return longest

nums = [1, 9, 3, 10, 4, 20, 2]
print(Solution().longestConsecutive(nums)) #Output : 4
