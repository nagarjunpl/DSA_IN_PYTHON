class Solution:
    def merge(self, nums1, m, nums2, n):
        # Remove the extra zeroes from nums1 and keep only the first m elements
        nums1[:] = nums1[:m]
        
        # Add elements of nums2 to nums1
        nums1.extend(nums2)
        
        # Sort nums1 in place
        nums1.sort()

        # Print the merged list
        print("Merged nums1:", nums1)


# ----- Input -----
nums1 = list(map(int, input("Enter nums1 (space-separated, with extra 0s at end): ").split()))
m = int(input("Enter m (number of valid elements in nums1): "))
nums2 = list(map(int, input("Enter nums2 (space-separated): ").split()))
n = int(input("Enter n (length of nums2): "))

# ----- Process -----
sol = Solution()
sol.merge(nums1, m, nums2, n)
