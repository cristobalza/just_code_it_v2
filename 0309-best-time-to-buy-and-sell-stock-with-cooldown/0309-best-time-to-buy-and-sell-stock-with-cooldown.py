class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        prices = [1,2,3,0,2]
                          i  

                       0 
                    buy.   cooldown
                -1
            sell.   cooldown
            +1
                cooldown
                 +1
              sell
              +1
              i == 4

        """
        # Dynamic Programming

        def dfs(i, is_buying):
            if i >= len(prices):
                return 0

            if (i, is_buying) in memo:
                return memo[(i, is_buying)]

            if is_buying:
                buy = dfs(i + 1, not is_buying) - prices[i]
                cooldown = dfs(i + 1, is_buying)
                memo[(i, is_buying)] = max(buy, cooldown)

            else:
                sell = dfs(i + 2, not is_buying) + prices[i]
                cooldown = dfs(i + 1, is_buying)
                memo[(i, is_buying)] = max(sell, cooldown)

            return memo[(i, is_buying)]
        
        memo = {} # store (visited index, buy or sell state): max profit
        return dfs(0, True)