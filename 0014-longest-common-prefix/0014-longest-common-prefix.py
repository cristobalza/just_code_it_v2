class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        """

        Input: strs = ["flower","flow","flight"]

        """
        
        res_word = ""

        for i, ch in enumerate(strs[0]):
            for word in strs[1:]:
                if i == len(word) or ch != word[i]:
                    return res_word

            res_word += ch

        return res_word