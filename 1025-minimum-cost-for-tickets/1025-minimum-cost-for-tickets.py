class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Memoization

        def dfs(i):
            if i == len(days):
                return 0

            if i in memo:
                return memo[i]

            res = float("inf")
            j = i

            for cost, duration in zip(costs, [1, 7, 30]):
            
                while j < len(days) and days[j] < days[i] + duration:
                    j += 1

                res = min(res, cost + dfs(j))

            memo[i] = res
            return memo[i]

        memo = {}
        return dfs(0)