class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Gauss Law - sum of the n digits
        # (n  / 2) * (n + 1)

        l, r = 1, n
        res = 0

        while l <= r:
            mid = (l + r) // 2
            sum_coins = (mid / 2) * (mid + 1)

            if sum_coins > n:
                r = mid - 1
            else:
                l = mid + 1
                res = max(res, mid)
            
        return res