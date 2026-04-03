class Solution:
    def search(self, nums, k):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == k:
                return m

            if nums[l] <= nums[m]:  # left sorted
                if nums[l] <= k < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:  # right sorted
                if nums[m] < k <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1

nums = [4,5,6,7,0,1,2]
k = 5
print(Solution().search(nums, k)) # Output: 1
