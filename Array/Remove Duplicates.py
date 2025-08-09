class Solution:
    def removeDuplicates(self, nums):
        # If the list is empty, return 0 (no elements)
        if not nums:
            return 0
            
        # The first element is always unique
        k = 1
        
        # Start from index 1 and compare each element with the previous one
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                # Place this unique element at index k
                nums[k] = nums[i]
                # Move k forward
                k += 1
                
        # Return the count of unique elements
        return k
                
# Example usage:
nums = [1, 1, 2]
a = Solution()

k = a.removeDuplicates(nums)

print(k, end=", ")
print(f"nums = {nums[:k]}")
