class Solution:
    def romanToInt(self, s: str) -> int:
        vls = {
            'I':1, 'V':5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        for i in range(len(s)):
            if i < len(s)-1 and vls[s[i]] < vls[s[i+1]]:
                total -= vls[s[i]]
            else:
                total += vls[s[i]]

        return total

sol = Solution()
# examples
print(sol.romanToInt("III"))     # 3
print(sol.romanToInt("IV"))      # 4
print(sol.romanToInt("IX"))      # 9
print(sol.romanToInt("LVIII"))   # 58
print(sol.romanToInt("MCMXCIV")) # 1994
