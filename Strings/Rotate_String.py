class Solution:    
    def rotateString(self, s, goal):
        tot_str = s + s
        if goal in tot_str:
            return True
        else:
            return False
