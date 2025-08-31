class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """

        Input: haystack = "sadbutsad", needle = "sad"
                           i
                           i + len(needle) < len(haystack) and haystack[i: i + len(needle)] == needle
                                        return i
                           needle[0] == haystack[i]
        """
        h_size, n_size = len(haystack), len(needle)

        for i in range(h_size):
            if needle[0] == haystack[i]:
                if i + n_size <= h_size and haystack[i: i + n_size] == needle:
                    return i

        return -1
        