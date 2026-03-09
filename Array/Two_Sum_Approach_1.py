class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list1 = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i,j]

nums = [2, 7, 11, 15]
target = 9
obj = Solution()
print(obj.twoSum(nums, target)) # Output : [0, 1]
