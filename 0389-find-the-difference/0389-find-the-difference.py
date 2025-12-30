class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        arr_s, arr_t = [0]* 26, [0]* 26

        for ch in s:
            arr_s[ord(ch) - ord("a")] += 1
        
        for ch in t:
            arr_t[ord(ch) - ord("a")] += 1
         
        lst = [chr(i)  for i in range(ord('a'), ord('z') + 1)]

        for i, ch in enumerate(lst):
            if arr_s[i] != arr_t[i]:
                return ch
