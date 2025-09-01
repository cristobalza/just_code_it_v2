class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.strip()
        if len(s) == 0:
            return 0

        sign = 1 if s[0] != "-" else -1
        res = 0

        for i, ch in enumerate(s):
            if i == 0 and ch in ["-", "+"]:
                continue
            if ch.isdigit():
                res = res * 10 + int(ch)
            else:
                break

        res = sign * res

        if res <= (-2)**31:
            res = (-2)**31
        elif res >= (2**31) - 1:
            res = (2**31) - 1
        
        return res
        