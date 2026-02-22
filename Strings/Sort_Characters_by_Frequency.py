class Solution:
    def frequencySort(self, s):
        freq={}

        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        result = sorted(freq.keys(), key = lambda x: (-freq[x], x))

        return result

sol = Solution()

print(sol.frequencySort("tree"))     # ['e', 'r', 't']
print(sol.frequencySort("raaaajj"))  # ['a', 'j', 'r']
