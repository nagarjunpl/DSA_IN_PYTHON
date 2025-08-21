class Solution:
    def bubble_sort(self, lst):
        has_swapped = True
        # if no swap occurred, lst is sorted
        while has_swapped:
            has_swapped = False
            for i in range(len(lst) - 1):
                if lst[i] > lst[i + 1]:
                    # Swap adjacent elements
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    has_swapped = True

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
sol = Solution()
print("Original:", arr)
sol.bubble_sort(arr)
print("Sorted:", arr)



