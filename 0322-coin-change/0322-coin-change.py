class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(total):
            if total == 0:
                return 0
            if total in memo:
                return memo[total]
            fewest_number_res = float("inf")
            for coin in coins:
                if total - coin >= 0:
                    fewest_number_res = min(fewest_number_res, 1 + dp(total - coin))
            memo[total] = fewest_number_res
            return fewest_number_res

        res = dp(amount)
        return res if res != float("inf") else -1