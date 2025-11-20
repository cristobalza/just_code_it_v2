class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # Top Down

        memo = {}

        def dfs(amount):
            
            if amount == 0:
                return 0

            if amount in memo:
                return memo[amount]

            res = float("inf")

            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))

            memo[amount] = res

            return memo[amount]

        min_amount = dfs(amount)
        return min_amount if min_amount != float("inf") else -1 