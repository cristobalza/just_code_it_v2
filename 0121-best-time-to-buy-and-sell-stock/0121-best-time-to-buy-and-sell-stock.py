class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0
        n = len(prices)
        l = 0

        for r in range(n):

            while prices[r] - prices[l] < 0 and l < r:
                l += 1

            res = max(res, prices[r] - prices[l])

        return res

                
                