class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # Memoization

        def dfs(i, amount):

            # Base case
            if i == len(coins) or amount < 0:
                return 0

            if amount == 0:
                return 1

            if (i, amount) in memo:
                return memo[(i, amount)]

            # Recursive call:
            #     1. Try current coin
            #     2. Skip current coin
            memo[(i, amount)] = dfs(i, amount - coins[i]) + dfs(i + 1, amount)

            return memo[(i, amount)]

        memo = {}
        return dfs(0, amount)