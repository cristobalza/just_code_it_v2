class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        curr = 0
        for e in w:
            curr += e
            self.prefix_sum.append(curr)

        self.n = len(self.prefix_sum)
        

    def pickIndex(self) -> int:
        # Binary Search

        target = random.randint(0, self.prefix_sum[-1])

        l, r = 0, self.n - 1

        while l < r:
            m = (l + r) // 2
            if self.prefix_sum[m] <= target:
                l = m + 1
            else:
                r = m

        return l

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()