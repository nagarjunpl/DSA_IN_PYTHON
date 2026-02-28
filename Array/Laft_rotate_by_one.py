class Solution:
    def rotateArrayByOne(self, nums):
        first = nums[0]

        for i in range(len(nums) - 1):
            nums[i] = nums[i + 1]

        nums[-1] = first
        return nums


nums = [1, 2, 3, 4, 5]
obj = Solution()
result = obj.rotateArrayByOne(nums)

print("Input:  [1, 2, 3, 4, 5]")
print("Output:", result)
