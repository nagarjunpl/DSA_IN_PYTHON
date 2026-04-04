class Solution:
    def search(self, nums, k):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == k:
                return True
              
            if nums[l] == nums[m] == nums[r]:
                l += 1
                r -= 1
            elif nums[l] <= nums[m]:  # left sorted
                if nums[l] <= k < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:  # right sorted
                if nums[m] < k <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return False

nums = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
k = 7
print(Solution().search(nums, k)) # Output: True
