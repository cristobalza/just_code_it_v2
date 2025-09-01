class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def helper(word):
            lst = [0] * 26
            
            for ch in word:
                lst[ord(ch) - ord("a")] += 1
                
            return lst  

        if len(s) != len(t):
            return False
        
        return helper(s) == helper(t)