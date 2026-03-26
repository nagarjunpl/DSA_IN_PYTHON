class Solution:
    def subarraySum(self, nums, k):
        count = 0
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                if total == k:
                    count += 1
        return count

nums = [1, 2, 3]
k = 3
obj = Solution()
print(obj.subarraySum(nums, k))  # Output: 2
