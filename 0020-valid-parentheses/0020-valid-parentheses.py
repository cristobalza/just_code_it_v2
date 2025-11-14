class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {
            '(': ')', 
            '{': '}', 
            '[': ']'
        }

        stack = []

        for c in s:
            if c in hmap:
                stack.append(c)
            else:
                if not stack or hmap[stack[-1]] != c:
                    return False

                stack.pop()

        return True if len(stack) == 0 else False