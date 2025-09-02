class Solution:
    def reverseWords(self, s: str) -> str:
        components = [comp for comp in s.split(" ") if comp]

        return " ".join(components[::-1])