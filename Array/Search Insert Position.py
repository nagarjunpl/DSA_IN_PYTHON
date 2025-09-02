class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Initialize search boundaries
        left, right = 0, len(nums) - 1

        # Standard binary search
        while left <= right:
            mid = (left + right) // 2  # Find the middle index

            if nums[mid] == target:
                # If target is found, return its index
                return mid
            elif nums[mid] < target:
                # If target is greater, ignore left half
                left = mid + 1
            else:
                # If target is smaller, ignore right half
                right = mid - 1

        # If target not found, left will be the correct insert position
        return left
