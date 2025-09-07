class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        """

        Input: numRows = 5

        i = 0

        [1]

        1 = 1
         0 1
        [1 1]


        i = 2
         0 1 2
        [1 2 1 ]


        Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

        """
        res = [] 
        dp = [1]
        res.append(dp)

        for i in range(numRows - 1):
            prev = res[-1]
            dp = [1] * (len(prev) + 1)
            for j in range((len(prev) + 1)):
                if j == 0 or j == (len(prev)):
                    continue
                dp[j] = prev[j- 1] + prev[j]

            res.append(dp)

        return res

        