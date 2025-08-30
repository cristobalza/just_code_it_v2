class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """

        coins = [1,2,5], amount = 11

        {}

        or use an array to store the minimum number of coins given ith amount
        
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        dp[3] = 2
        dp[4] = 2
        dp[5] = 1
        dp[6] = 2
        dp[7] = 2
        dp[8] = 3
        dp[9] = 3
        dp[10] = 2
        dp[11] = 3

        iterate from 0 to amount + 1

        dp[7] = 1 + dp[6] = 1 + 2 = 3 but 7 - 3 = 4 and we've computed dp[4] => dp[7] = 1 + dp[4] = 1 + 1 = 2//



        for each coin - substract coin value by the index
        
  
         1 + 2 (3)+5(8)+end 
         +.  +
         1   2 (5)
         (2)+ 2
         +
         1
         (3)
         
        """

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        return dp[amount] if dp[amount] != float('inf') else -1
                

