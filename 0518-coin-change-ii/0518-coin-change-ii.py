class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # Memoization

        def dfs(i, curr_amount):

            # Base case
            if i == len(coins) or curr_amount > amount:
                return 0

            if curr_amount == amount:
                return 1

            if (i, curr_amount) in memo:
                return memo[(i, curr_amount)]

            # Recursive call:
            #     1. Try current coin
            #     2. Skip current coin
            memo[(i, curr_amount)] = dfs(i, curr_amount + coins[i]) + dfs(i + 1, curr_amount)

            return memo[(i, curr_amount)]

        memo = {}
        return dfs(0, 0)