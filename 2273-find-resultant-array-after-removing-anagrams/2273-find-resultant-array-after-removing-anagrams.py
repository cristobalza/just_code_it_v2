class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = []
        prev = None

        for word in words:
            curr = [0] * 26
            for ch in word:
                curr[ord(ch) - ord('a')] += 1

            if prev != curr:
                res.append(word)
            prev = curr

        return res
