class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        parenthesis_dict = {
            "(": ")",
            "[": "]",
            "{": "}",

        }

        for char in s:
            if char in parenthesis_dict.keys():
                stack.append(char)
            else:
                if len(stack) == 0 or char != parenthesis_dict.get(stack[-1]):
                    return False
                stack.pop()
                
        return True if len(stack) == 0 else False