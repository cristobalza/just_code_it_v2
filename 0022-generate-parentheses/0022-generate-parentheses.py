class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def backtrack(start, end, subset):

            if start == end == n:
                res.append("".join(subset))
                return

            if start < n:
                subset.append("(")
                backtrack(start + 1, end, subset)
                subset.pop()
            if end < start:
                subset.append(")")
                backtrack(start, end + 1, subset)
                subset.pop()
            
            return

        res = []
        backtrack(0, 0, [])
        return res
        