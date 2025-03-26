class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False 

        s_list = [0] * 26
        t_list = [0] * 26

        for char in s:
            s_list[ord(char) - ord("a")] += 1

        for char in t:
            t_list[ord(char) - ord("a")] += 1

        return s_list == t_list