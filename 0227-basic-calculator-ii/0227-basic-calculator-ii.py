class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        operation = "+"

        for i, ch in enumerate(s):
            if ch == "":
                continue

            if ch.isdigit():
                num = num * 10 + int(ch)

            if ch in ('+', '-', '*', '/') or i == len(s) - 1:
                if operation == '+':
                    stack.append(num)
                if operation == '-':
                    stack.append(-num)
                if operation == '*':
                    stack.append(stack.pop() * num)
                if operation == '/':
                    stack.append(int(stack.pop() / num))
                
                num = 0
                operation = ch
        
        return sum(stack)

            

                
