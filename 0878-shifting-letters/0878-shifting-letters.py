class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)

        # create a suffix array
        curr_sum = 0
        suffix_arr = [0] * n
        for i in range(n - 1, -1, -1):
            curr_sum += shifts[i]
            suffix_arr[i] = curr_sum

        res = []
        for i in range(n):
            char_unicode = ord(s[i]) - ord('a') # get original unicode

            new_char_unicode = (suffix_arr[i] + char_unicode) % 26 # calculate new unicode

            res.append(chr(new_char_unicode + ord("a"))) # convert back to letter
        
        return "".join(res)

