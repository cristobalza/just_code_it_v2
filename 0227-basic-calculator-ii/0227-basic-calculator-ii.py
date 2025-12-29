class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack = []
        num = 0
        operation = '+'
        
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            
            # Process when we hit an operator or end of string
            if ch in ['+', '-', '*', '/'] or i == len(s) - 1:
                if operation == '+':
                    stack.append(num)
                elif operation == '-':
                    stack.append(-num)
                elif operation == '*':
                    stack.append(stack.pop() * num)
                elif operation == '/':
                    stack.append(int(stack.pop() / num))
                
                if i < len(s) - 1:
                    operation = ch
                num = 0 # reset the num
        
        res = 0
        for val in stack:
            res += val
        
        return res