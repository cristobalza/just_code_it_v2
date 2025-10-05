class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def backtrack(_open, _close, subset):

            if _open == _close == n:
                res.append("".join(subset[::]))
                return

            if _open < n:
                subset.append("(")
                backtrack(_open + 1, _close, subset)
                subset.pop()

            if _close < _open:
                subset.append(")")
                backtrack(_open, _close + 1, subset)
                subset.pop()

            return 


        res = []
        
        backtrack(0, 0, [])

        return res

        