class Solution:
    def merge(self, nums1, m, nums2, n):
        # Remove the extra zeroes from nums1 and keep only the first m elements
        nums1[:] = nums1[:m]
        
        # Add elements of nums2 to nums1
        nums1.extend(nums2)
        
        # Sort nums1 in place
        nums1.sort()
