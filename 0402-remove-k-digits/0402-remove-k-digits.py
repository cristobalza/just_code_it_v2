class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        num = "1432219", k = 3
                    i

        num = 2
        stack[-1]> num 2 > 1
        k = 0
        stack [1, 2, 1, 9]

        """
        # Monotically decreasing

        stack = []

        for charnum in num:
            while stack and stack[-1] > charnum and k > 0:
                stack.pop()
                k -= 1
            if stack or charnum != "0":
                stack.append(charnum)

        stack = stack[:-k] if k else stack
        return "".join(stack).lstrip('0') if stack  else '0'