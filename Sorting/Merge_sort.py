class Solution:
    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])

        i = j = 0
        result = []

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        return result + left[i:] + right[j:]

nums = [5, 3, 5, 56, 0, 8, 1]
obj = Solution()
print(obj.mergeSort(nums)) #output: [0, 1, 3, 5, 5, 8, 56]
