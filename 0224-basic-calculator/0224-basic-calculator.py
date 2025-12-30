class Solution:
    def calculate(self, s: str) -> int:
        """

        s = "(1+(4+5+2)-3)+(6+8)"
                         i 

        stack = [0, 1, 10, 1]

        sign = -1
        num = 3

        res = 0


        """

        stack = []
        res = 0
        num = 0
        sign = 1

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)

            if ch == "+":
                res += sign * num
                sign = 1
                num = 0

            if ch == "-":
                res += sign * num 
                sign = -1
                num = 0

            if ch == "(":
                stack.append(res)
                stack.append(sign)

                res = 0 # reset res and sign 
                sign = 1
            
            elif ch == ")":
                res += sign * num
                num = 0 

                res *= stack.pop() # sign
                res += stack.pop() # last nums

        res += sign * num

        return res