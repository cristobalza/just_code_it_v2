class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        def helper(word):
            lst = [0] * 26

            for ch in word:
                lst[ord(ch) - ord("a")] += 1
            
            return lst

        ransomNote_list = helper(ransomNote)
        magazine_list = helper(magazine)

        for i in range(26):
            if ransomNote_list[i] > magazine_list[i]:
                return False
        
        return True