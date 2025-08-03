class Solution:
    def findNumbers(self, nums):
        # Initialize counter to count numbers with even number of digits
        count_next = 0

        # Iterate through each number in the list
        for num in nums:
            count = 0  # Reset digit count for each number

            # Convert number to string and count its digits
            for no in str(num):
                count += 1

            # If the number of digits is even, increment the result counter
            if count % 2 == 0:
                count_next += 1

        # Return the final count of numbers with even number of digits
        return count_next

# Take user input as a list (e.g., [12, 345, 2, 6, 7896])
user_input = input("Enter a list of numbers (e.g., [12, 345, 2, 6, 7896]): ")

# Clean the input and convert it to a list of integers
clean_input = user_input.replace('[', '').replace(']', '').replace(',', ' ')
nums = list(map(int, clean_input.strip().split()))

# Create an instance of the class
so = Solution()

print("Count of numbers with even number of digits:", so.findNumbers(nums))
