class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        stack = []

        for ch in s:
            if ch in ["(", "{", "["]:
                stack.append(ch)
            else:
                if not stack or ch != hmap[stack[-1]]:
                    return False
                stack.pop()

        return True if len(stack) == 0 else False