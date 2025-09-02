class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        components = [comp for comp in path.split("/") if comp and comp != "."]

        for comp in components:
            if comp == "..":
                if stack:
                    stack.pop()
            
            else:
                stack.append(comp)

        return "/" + "/".join(stack)