class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Given
            s - string that needs to map to t
            t - string that is the target

         s = "egg", t = "add"
                i          i

        hmap { 
            e: a
            g: d

        }

        """
        if len(s) != len(t):
            return False

        hmap = {}
        for i in range(len(s)):
            if s[i] in hmap:
                if hmap[s[i]] != t[i]:
                    return False

            else:
                hmap[s[i]] = t[i]


        hmap = {}
        for i in range(len(t)):
            if t[i] in hmap:
                if hmap[t[i]] != s[i]:
                    return False

            else:
                hmap[t[i]] = s[i]

        return True

        