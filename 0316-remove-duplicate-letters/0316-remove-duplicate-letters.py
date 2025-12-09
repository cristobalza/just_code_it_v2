class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        Check if letter exist or has been visited
            continue
        Check the smallest lexicographical order
            Then check for the index if its less than the current index
                pop it from stack and update the index value

        s = "bcabc"
                i

        while s[i] < stack[-1] and i > hmap[stack[-1]]:
            pop

        hmap{
            b: 0
            c: 1
            a: 2

        }

        stack = [b, c, a]
             

        """
        hmap = {ch: i for i, ch in enumerate(s)} # last index occurred 

        stack = [] # store characters
        visited = set() # check visited characters

        for i, ch in enumerate(s):
            if ch in visited:
                continue

            while stack and s[i] < stack[-1] and i < hmap[stack[-1]]:
                stack_top = stack.pop()
                visited.remove(stack_top)

            stack.append(ch)
            visited.add(ch)

        return "".join(stack)

