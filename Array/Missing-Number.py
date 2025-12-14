# METHOD 1 :
class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        total_sum = n * (n + 1) // 2
        array_sum = sum(nums)
        return total_sum - array_sum


# METHOD 2
class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        for i in range(n + 1):
            if i not in nums :
                return i
