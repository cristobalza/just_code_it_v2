class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Input: s = "   fly me   to   the moon  "
                                              i

        """
        # s = s.strip()
        n = len(s) - 1

        while n >= 0 and s[n] == " ":
            n -= 1
        
        # s = s.split(" ")
        end = n
        start = n
        while start >= 0 and s[start].isalnum():
            start -= 1

        return end - start