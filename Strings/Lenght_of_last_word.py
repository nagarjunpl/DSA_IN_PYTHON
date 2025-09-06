class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new = s.strip().split()   # removes spaces from ends, splits by spaces into list
        rev = new[::-1]           # reverses the list
        for j in rev[0:2]:        # takes the first word from the reversed list
            return len(j)         # returns its length
