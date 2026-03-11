class Solution:
    def insertionSort(self, nums):
        n = len(nums)
        for i in range(1, n):
            key = nums[i]
            j = i - 1
            while key < nums[j] and j >= 0:
                nums[j+1] = nums[j]
                j -= 1
            nums[j + 1] = key

        return nums

nums = [12, 11, 13, 5, 6]
obj = Solution()
print(obj.insertionSort(nums)) # Output: [5, 6, 11, 12, 13]
