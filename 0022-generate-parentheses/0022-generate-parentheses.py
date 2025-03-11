class Solution:
    def generateParenthesis(self, n: int) -> List[str]:


        def backtrack(start, end, stack):
            nonlocal res, n

            if start == end == n:
                res.append("".join(stack))
                return 
            
            if start < n:
                stack.append("(")
                backtrack(start + 1, end, stack)
                stack.pop()
            if end < start:
                stack.append(")")
                backtrack(start, end + 1, stack)
                stack.pop() 

        res = []
        backtrack(0, 0, [])
        return res


