class Solution:
    def maxProfit(self, arr):
        min_price = float('inf')
        max_profit = 0

        for price in arr:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)

        return max_profit

arr = [3, 8, 1, 4, 6, 2]
obj = Solution()
print(obj.maxProfit(arr)) # 5
