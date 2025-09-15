class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_set = set([ch for ch in brokenLetters])
        text_list = text.split(" ")
        res = 0
        for word in text_list:
            is_broken = False
            for ch in word:
                if ch in broken_set:
                    is_broken = True
                    break

            if not is_broken:
                res += 1

        return res
        