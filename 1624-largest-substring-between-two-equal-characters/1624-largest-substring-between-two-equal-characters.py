class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        hmap = {} # store ch: idx
        stack = [] # store ch, idx

        for i, ch in enumerate(s):
            if ch in hmap:
                stack.append((ch, hmap[ch]))
            else:
                hmap[ch] = i

        res = -1

        while stack:
            ch, l = stack.pop()

            for r in range(l, len(s)):
                if s[r] == s[l]:
                    res = max(res, r - l - 1)
        
        return res
        

        

            
        