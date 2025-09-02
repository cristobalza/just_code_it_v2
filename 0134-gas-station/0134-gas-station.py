class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Input: gas =  [1,2,3,4,5], 
               cost = [3,4,5,1,2]

               diff = [-2.-2,-2,3,5]

        """

        if sum(gas) < sum(cost):
            return -1

        total = 0
        res = 0

        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = i + 1

        return res