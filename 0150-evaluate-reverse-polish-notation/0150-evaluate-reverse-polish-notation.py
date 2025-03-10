class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        ["4","13","5","/","+"]
              |       |


        """

        stack = []

        for token in tokens:
            if token == "+":
                digit_a = stack.pop()
                digit_b = stack.pop()
                stack.append(digit_a + digit_b)
            elif token == "-":
                digit_a = stack.pop()
                digit_b = stack.pop()
                stack.append(digit_b - digit_a)
            elif token == "*":
                digit_a = stack.pop()
                digit_b = stack.pop()
                stack.append(digit_a * digit_b)
                print(stack[-1])
            elif token == "/":
                digit_a = stack.pop()
                digit_b = stack.pop()
                stack.append(int(digit_b / digit_a))
            else:
                stack.append(int(token))
        
        return stack[0]


        