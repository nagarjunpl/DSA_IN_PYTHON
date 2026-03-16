class Solution:
    def heightChecker(self, heights):
        # Counter to track how many positions differ
        count = 0
        # Make a copy of the original list
        arr = heights[:]
        # Bubble Sort
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
        # Compare sorted array with original array
        for i in range(len(arr)):
            if arr[i] != heights[i]:
                count += 1

        return count

# Input
heights = [1, 1, 4, 2, 1, 3]
# Create object
obj = Solution()
# Call function
result = obj.heightChecker(heights)
# Output
print("Number of students in wrong position:", result) #Output: Number of students in wrong position: 3
