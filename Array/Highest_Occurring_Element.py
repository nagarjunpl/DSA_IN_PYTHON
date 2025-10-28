class Solution:
    def highestOccurringElement(self, nums):
        max_count = 0
        ans = min(nums)  
        
        for num in nums:
            count = nums.count(num) 
            if count > max_count or (count == max_count and num < ans):
                max_count = count
                ans = num
        return ans

a = Solution()
print(a.highestOccurringElement([1, 2, 2, 3, 3, 3]))  # Output: 3
print(a.highestOccurringElement([4, 4, 5, 5, 6]))     # Output: 4
