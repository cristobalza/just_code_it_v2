class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        Given
            nums: list of strings that contain digits
            k; integer that set the number of strings possible to remove

        num = "1432219", k = 3
                    i

        montonic increasing stack

        stack = [1, 2, 1, 9]
        k = 0
        num = 2

        while stack and stack[-1] >= num and k > 0:
            stack.pop()
            k -= 1

        stack.append(num)
               
        """

        stack = []

        for i, ch_num in enumerate(num):
            
            while stack and int(stack[-1]) > int(ch_num) and k > 0:
                stack.pop()
                k -= 1
            
            stack.append(ch_num)

        if k > 0:
            stack = stack[:-k]  # Remove last k elements

        res = "".join(stack).lstrip("0")
        return res if res != "" else "0"


        