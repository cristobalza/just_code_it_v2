class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")

        res = 0

        i, n = 0, len(s)

        stack = []

        num, operation = 0, "+"

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)

            if ch in ['+', '-', '*', '/'] or i == len(s) - 1: # check operations or end of string
                if operation == "+":
                    stack.append(num)
                if operation == "-":
                    stack.append(-num)
                if operation == "*":
                    last_num = stack.pop()
                    stack.append(last_num * num)
                if operation == "/":
                    last_num = stack.pop()
                    stack.append(int(last_num / num))

                operation = ch
                num = 0

        res = 0
        for val in stack:
            res += val
        return res
