class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def helper(word):
            res = [0] * 26

            for char in word:
                res[ord(char) - ord("a")] += 1
            
            return res

        s_res, t_res = helper(s), helper(t)

        return s_res == t_res