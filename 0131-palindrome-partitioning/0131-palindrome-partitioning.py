class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def backtrack(i, subset):
            if i >= len(s):
                res.append(subset[::])
                return

            for j in range(i, len(s)):
                # check palindrome
                if check_palindrome(i, j):
                    subset.append(s[i: j + 1])
                    backtrack(j + 1, subset)
                    subset.pop()
                    
            return

        def check_palindrome(i, j):
            l, r = i, j

            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True

        res = []
        backtrack(0, [])
        return res
            
                

        