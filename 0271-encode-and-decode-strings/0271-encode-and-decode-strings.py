class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""

        for i, word in enumerate(strs):
            res = res + str(len(word)) + "?" + word

        return res
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        l = 0
        while l < len(s):
            r = l
            while r < len(s) and s[r] != "?":
                r += 1

            num = int(s[l:r])
            word = s[r + 1: r + 1 +num]

            res.append(word)

            l = r + 1 + num

        return res

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))