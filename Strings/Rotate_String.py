class Solution:
    # Method 1 
    def rotateString(self, s, goal):
        tot_str = s + s
        if goal in tot_str:
            return True
        else:
            return False

    # Method 2
    def rotateString(self, s, goal):
        for i in range(len(s)):
            rotated = s[i:] + s[:i]
            if rotated == goal:
                return True
        
        return False
