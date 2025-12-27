class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """

        nums = [3,1,5,8]


        [3, 5, 8]


        [3, 8]

        [8]



        nums = [3,1,5,8]


        [1, 5, 8]40       [3, 5, 8]120           [3,1, 8]24      [3,1,5]15

       [5,8][1,8][1,5]    [5,8]40[3,8]24[3,5]15     [1,8][3,8][3,1]    [3,1][3,5][3,1]

                         165,168. 1 




        """

        nums = [1] + nums + [1]
        memo = {}

        def dfs(l, r):
            if l + 1 == r:
                return 0
            
            if (l, r) in memo:
                return memo[(l, r)]

            max_coins = 0
            for i in range(l + 1, r):
                coins = nums[l] * nums[i] * nums[r]
                coins += dfs(l, i) + dfs(i, r)
                max_coins = max(max_coins, coins)
            
            memo[(l, r)] = max_coins

            return memo[(l, r)]

        return dfs(0, len(nums) - 1)

