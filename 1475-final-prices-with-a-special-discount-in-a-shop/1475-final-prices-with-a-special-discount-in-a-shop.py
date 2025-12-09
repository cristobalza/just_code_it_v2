class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # Monotonic decreasing (next smaller)

        stack = [] # store original values
        hmap = {} # store original values: idx
        res = [p for p in prices]

        for i, p in enumerate(prices):

            while stack and stack[-1] >= p:
                stack_top = stack.pop()
                original_idx = hmap[stack_top]
                res[original_idx] = stack_top - p

            stack.append(p)
            hmap[p] = i

        return res