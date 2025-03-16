class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        l, r = 1, max(piles)

        res = r

        while l <= r:
            speed_k = (l + r) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / speed_k)

            if hours <= h:
                res = speed_k
                r = speed_k - 1
            else:
                l = speed_k + 1

        return res

                


