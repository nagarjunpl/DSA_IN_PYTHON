class Solution:
    def singleNumber(self, nums):
        single_number = 0

        for num in nums:
            single_number ^= num
            
        return single_number

nums = [4,1,2,1,2]
obj = Solution()
print(obj.singleNumber(nums)) # Output : 4
