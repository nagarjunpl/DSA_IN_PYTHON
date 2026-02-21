class Solution:    
    def anagramStrings(self, s, t):
        if len(s) != len(t):
            return False

        for i in range(len(t)):
            if t[i] not in s:
                return False
            else:
                s = s.replace(t[i], '', 1)   # it remove one occurrence in s
        
        return True
