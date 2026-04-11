class Solution:
    def rearrangeArray(self, nums):
        pos = []
        neg = []
        for x in nums:
            if x >= 0:
                pos.append(x)
            else:
                neg.append(x)
        result = []
        for i in range(len(pos)):
            result.append(pos[i])
            result.append(neg[i])
        return result

nums = [-4, 4, -4, 4, -4, 4]
print(Solution().rearrangeArray(nums)) # Output : [4 -4 4 -4 4 -4]
