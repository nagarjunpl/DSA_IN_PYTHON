class Solution:
    def removeElement(self, nums, val):
        k = 0  # pointer for the position of the next valid element
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # move valid element forward
                k += 1
        
        return k
        
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
obj = Solution()
k = obj.removeElement(nums, val)
print(k)      # 5
print(nums)   # [0, 1, 3, 0, 4, 0, 4, 2] -> first 5 elements correct

