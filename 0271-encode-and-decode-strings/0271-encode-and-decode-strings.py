class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        out_str = ""
        for _str in strs:
            out_str += str(len(_str)) + "?" + _str
        return out_str

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        l = 0
        out_list = []
        N = len(s)
        while l < N:
            r = l
            while r < N and s[r] != "?":
                r +=1 
            size = int(s[l:r])
            _str = s[r + 1: r + 1 + size]
            out_list.append(_str)
            l = r + 1 + size
        return out_list
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))