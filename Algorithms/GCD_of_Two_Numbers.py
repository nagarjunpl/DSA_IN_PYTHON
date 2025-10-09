class Solution:
    def GCD(self, n1, n2):
        if n1 < n2:
            smaller = n1
        else:
            smaller = n2

        for i in range(1, smaller + 1):
            # If i divides both numbers, it is a common divisor
            if (n1 % i == 0) and (n2 % i == 0):
                gcd = i  # Store the current common divisor

        return gcd

a = Solution()

# Call GCD function and print results
print(a.GCD(4, 6))   # Output: 2
print(a.GCD(9, 24))  # Output: 3
