class Solution:
    def isomorphicString(self, s : str, t : str) -> bool:
        if len(s) != len(t):
            return False

        map_s = {}
        map_t = {}

        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]

            # Check s->t mapping
            if c1 in map_s:
                if map_s[c1] != c2:
                    return False
            else:
                map_s[c1] = c2

            # Check t->s mapping
            if c2 in map_t:
                if map_t[c2] != c1:
                    return False
            else:
                map_t[c2] = c1
        
        return True
    
