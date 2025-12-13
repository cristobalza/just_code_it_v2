class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = []
        prev = None

        for word in words:
            curr = sorted(word)

            if prev != curr:
                res.append(word)
                prev = curr

        return res
