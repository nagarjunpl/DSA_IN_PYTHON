class Solution:
    def romanToInt(self, s: str) -> int:
        # Mapping of Roman numeral symbols to integer values
        values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
      
        total = 0  # variable to store the final result
        
        # Loop through the string up to the second-to-last character
        for i in range(len(s) - 1):
            if values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]  # subtract the current value
            else:
                total += values[s[i]]  # otherwise, just add it
        
        # Add the last numeral (always added, never subtracted)
        total += values[s[-1]]
        
        return total  # return the computed
