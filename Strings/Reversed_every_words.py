class Solution:
    def reverseWords(self, s: str) -> str:
        st = s.split()
        rev = []
        for word in st:
            rev.insert(0, word)

        return " ".join(rev)

s = "I love Python"
obj = Solution()
result = obj.reverseWords(s)
print("Output:", result) # Output: Python love I
