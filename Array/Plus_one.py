class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Start from the last digit and move left
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:      # If digit < 9, just increment and return
                digits[i] += 1
                return digits
            digits[i] = 0          # If digit == 9, set to 0 and carry over
        
        # If we exit loop, all digits were 9
        return [1] + digits
