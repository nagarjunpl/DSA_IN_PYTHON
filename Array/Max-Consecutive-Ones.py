class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0  # To store the highest number of 1s in a row
        count = 0      # To count current 1s in a row

        for num in nums:
            if num == 1:
                count += 1           # Add 1 to count if the number is 1
                if count > max_count:
                    max_count = count  # Update max_count if count is bigger
            else:
                count = 0            # If number is 0, reset count to 0

        return max_count

# Example use
nums = [1, 1, 0, 1, 1, 1]
a = Solution()
print(a.findMaxConsecutiveOnes(nums))
