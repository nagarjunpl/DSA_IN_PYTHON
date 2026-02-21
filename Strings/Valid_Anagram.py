class Solution:    
    def anagramStrings(self, s, t):
        if len(s) != len(t):
            return False

        for i in range(len(t)):
            if t[i] not in s:
                return False
                break
        return True
