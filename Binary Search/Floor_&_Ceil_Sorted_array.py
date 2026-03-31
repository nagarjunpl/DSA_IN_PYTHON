class Solution:
    def getFloorAndCeil(self, nums, x):
        n = len(nums)
        floor = -1
        ceil = -1
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == x:
                return nums[mid], nums[mid]
              
            elif nums[mid] < x:
                floor = nums[mid]
                left = mid + 1
            else:
                ceil = nums[mid]
                right = mid - 1

        return floor, ceil

nums = [2, 4, 6, 8, 10, 12, 14]
x = 1
sol = Solution() 
floor, ceil = sol.getFloorAndCeil(nums, x)
print(floor, ceil) # Output : -1 2
