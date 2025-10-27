class Solution:
    def countFrequencies(self, nums):
        result = []
        checked = []  

        for num in nums:
            if num not in checked:
                count = nums.count(num)
                result.append([num, count])
                checked.append(num)      

        return result
      
a = Solution()
print(a.countFrequencies([1, 2, 2, 1, 3]))    # OUTPUT : [[1, 2], [2, 2], [3, 1]]
print(a.countFrequencies([5, 5, 5, 5]))       # OUTPUT : [[5, 4]]
