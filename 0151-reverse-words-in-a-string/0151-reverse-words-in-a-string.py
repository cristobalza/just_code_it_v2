class Solution:
    def reverseWords(self, s: str) -> str:

        res = ""

        components = [comp for comp in s.split(" ") if comp]

        for i in range(len(components) - 1, -1, -1):
            if i == 0:
                res += components[i]

            else:
                res += components[i]
                res += " "

        return res