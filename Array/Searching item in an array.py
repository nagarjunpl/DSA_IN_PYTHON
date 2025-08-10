class Solution:
    def validMountainArray(self, arr):
        n = len(arr)
        
        # Mountain needs at least 3 elements
        if n < 3:
            return False
        
        i = 0
        
        # Walk uphill
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
        
        # Peak can't be first or last
        if i == 0 or i == n - 1:
            return False
        
        # Walk downhill
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1
        
        # If we reached the end, it's a valid mountain
        return i == n - 1


# Take user input
arr = list(map(int, input("Enter numbers separated by space: ").split()))

sol = Solution()
if sol.validMountainArray(arr):
    print("Valid Mountain Array")
else:
    print("Not a Valid Mountain Array")
