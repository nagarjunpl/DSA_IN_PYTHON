class Solution:
    # Method 1: Using s + s trick (Optimal)
    def rotateString_method1(self, s, goal):
        if len(s) != len(goal):
            return False
        
        tot_str = s + s
        return goal in tot_str
    
    # Method 2: Brute force rotation
    def rotateString_method2(self, s, goal):
        if len(s) != len(goal):
            return False
        
        for i in range(len(s)):
            rotated = s[i:] + s[:i]
            if rotated == goal:
                return True
        
        return False

sol = Solution()

s = "abcde"
goal = "cdeab"
print("Method 1 Result:", sol.rotateString_method1(s, goal))
print("Method 2 Result:", sol.rotateString_method2(s, goal))
