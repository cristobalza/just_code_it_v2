class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {
            '(': ')', 
            '{': '}',
            '[': ']'
        }

        stack = []

        for char in s:
            if char in hmap:
                stack.append(char)
            else:
                if not stack or char != hmap[stack.pop()]:
                    return False


        return True if len(stack) == 0 else False

