class Solution:
    def sortColors(self, nums):
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:  # place 0's at the start
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:  # keep 1's in the middle
                mid += 1
            else:  # nums[mid] == 2, place 2's at the end
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
nums = [2, 0, 2, 1, 1, 0]
Solution().sortColors(nums)
print(nums)
