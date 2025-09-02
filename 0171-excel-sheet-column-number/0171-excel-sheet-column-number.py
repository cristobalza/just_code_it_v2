class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        """
        ord("B") - ord("A")

        """
        res = 0
        for i, ch in enumerate(columnTitle):
            if i == 0:
                res = ord(ch) - ord("A") + 1
            else:
                res = res * 26 + (ord(ch) - ord("A") + 1)

        return res

        