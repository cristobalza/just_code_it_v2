class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        first_word = strs[0]
        for i in range(len(first_word)): 
            for word in strs[1:]:
                if i == len(word) or word[i] != first_word[i]:
                    return res 

            res += first_word[i]

        return res


