class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
                                                                              i
        stack = [22]

        """
        stack = []
        operation = None

        for ch in tokens:
            if len(stack) >= 2 and ch in ["+", "-", "*", "/"]:
                operation = ch
                num2 = int(stack.pop())
                num1 = int(stack.pop())

                if operation == "+":
                    stack.append(num1 + num2)
                elif operation == "-":
                    stack.append(num1 - num2)
                elif operation == "*":
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1 / num2))
            
            else:
                stack.append(int(ch))

        return stack[0]

            