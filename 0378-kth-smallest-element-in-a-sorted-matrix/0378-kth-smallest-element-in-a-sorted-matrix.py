class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l, r, N = matrix[0][0], matrix[-1][-1], len(matrix)

        def less_k(mid):
            count = 0
            for row in range(N):
                val = bisect_right(matrix[row], mid)
                count += val
            return count

        while l < r:
            mid = (l+r)//2
            if less_k(mid) < k:
                l = mid + 1
            else:
                r = mid

        return l

        