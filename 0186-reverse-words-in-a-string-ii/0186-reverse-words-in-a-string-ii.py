class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def reverse_helper(l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        n = len(s)

        reverse_helper(0, n - 1)

        l = 0

        for r in range(n + 1):
            if r == n or s[r] == " ":
                reverse_helper(l, r - 1)
                l = r + 1

        
        

        
        