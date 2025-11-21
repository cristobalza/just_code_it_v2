class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        coins = [1,2,5], amount = 11


                        1
                       1 2 5
                       1 ...
                       1  6x   5
                       1       3x
                       1
                       ...
                       11x

        bottom up:

        dp: [0, inf, inf, ..., inf] * (amount + 1)
                 i 
        
        for i in range(1, n):
            if i - coin >= 0:
                dp[i] = min(dp[i], 1 + dp[i - coin])
        
        retun dp[-1] if possible

        dp : [float(")]
        O(coins * amount) time 
        O(coins * amount) space
        """

        dp = [float("inf")] * (amount + 1) 
        dp[0] = 0

        for i in range(1, (amount + 1)):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        return dp[-1] if dp[-1] != float("inf") else -1
