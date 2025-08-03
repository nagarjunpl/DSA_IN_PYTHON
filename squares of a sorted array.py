class Solution:
    def sortedSquares(self, nums):
        squared = []
        for num in nums:
            squared.append(num ** 2)
        sorted_square = sorted(squared)
        return sorted_square

# Take input from user
user_input = input("Enter numbers separated by space: ")
nums = list(map(int, user_input.strip().split()))

# Create object and call function
sol = Solution()
print(sol.sortedSquares(nums))
