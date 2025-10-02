class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        empty_bottles = 0
        drunk = 0

        while numBottles > 0:

            drunk += numBottles
            empty_bottles += numBottles
            numBottles = 0

            while empty_bottles >= numExchange:
                empty_bottles -= numExchange
                numBottles += 1
                numExchange += 1

        return drunk
        