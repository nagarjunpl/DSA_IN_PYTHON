class Solution:
    def heightChecker(self, heights) -> int:
        # Counter to track how many positions differ
        count = 0
        
        # Make a copy of the original list so we can sort it
        arr = heights[:]

        # Bubble sort implementation
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(arr) - 1):
                # Compare adjacent elements
                if arr[i] > arr[i + 1]:
                    # Swap if they are in the wrong order
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True  # Mark that a swap happened

        # Compare the sorted array with the original heights
        for j in range(len(arr)):
            if arr[j] != heights[j]:
                count += 1  # Increase count if mismatch found

        # Return total mismatches (students not in expected order)
        return count
# Example input
heights = [1, 1, 4, 2, 1, 3]

# Create an object of Solution
sol = Solution()

# Call the method and print the result
result = sol.heightChecker(heights)
print("Number of students in wrong position:", result)
