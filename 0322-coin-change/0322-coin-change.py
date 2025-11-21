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

        memoization:

        base case: amount == 0: return 0 or if amount in memo: return memo

        res = inf
        for coin in coins
            if  new_amount -> amount - coin >= 0
                    res = min(res, 1 + recursion call dfs( new_amount))
                                    add one more coin

        memo[amount] = res
        return memo[amount]

        O(coins^amount) time 
        O(amount) space
        """

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

        memo = {}

        min_number_coins = dfs(amount)

        return min_number_coins if min_number_coins != float("inf") else -1