class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # Bottom-up
        
        """
        amount = 5
        coins = [1, 2, 5]

          0 1 2 3 4 5
          - - - - - -          
       1 |1 0 0 0 0 0 
       2 |1 0 0 0 0 0
       5 |1 0 0 0 0 0
        """

        dp = [[0]* (len(coins) + 1) for _ in range(amount + 1)] 

        for c in range(len(coins) + 1):
            dp[0][c] = 1

        for i in range(1, amount + 1):
            for j in range(len(coins) - 1,  -1, -1):
                dp[i][j] = dp[i][j + 1] 
                if i - coins[j] >= 0:
                    dp[i][j] += dp[i - coins[j]][j]

        return dp[amount][0]
