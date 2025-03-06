class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis_dict = {
            '(': ')', 
            '{': '}', 
            '[': ']',
        }
        
        stack = []

        for char in s:
            if char in parenthesis_dict.keys():
                stack.append(char)
            else:
                if stack and parenthesis_dict[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
                    
        return True if len(stack) == 0 else False