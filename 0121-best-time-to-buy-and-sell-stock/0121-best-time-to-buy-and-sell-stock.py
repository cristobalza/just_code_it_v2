class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, r = 0, 1

        res = 0

        n = len(prices)

        while r < n:

            if prices[r] > prices[l]:

                res = max(res, prices[r] - prices[l])

            else:

                l = r

            r += 1

        return res