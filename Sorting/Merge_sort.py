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
            result.append(left[i] if left[i] < right[j] else right[j])
            if left[i] < right[j]:
                i += 1
            else:
                j += 1
    
        return result + left[i:] + right[j:]
    
obj = Solution()
print(obj.mergeSort([5,3,5,56,0,8,1]))
