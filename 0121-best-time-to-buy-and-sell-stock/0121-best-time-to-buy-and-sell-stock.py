class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """

        prices = [7,1,5,3,6,4]
                    l
                            r 

                prices[r] - prices[l] = 

        """

        l = 0
        res = 0

        for r in range(len(prices)):
            if prices[r] - prices[l] < 0:
                l = r
            res = max(res, prices[r] - prices[l])

        return res