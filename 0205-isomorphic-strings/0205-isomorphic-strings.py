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

        hmap_s, hmap_t = {}, {}
        for i in range(len(s)):
            if s[i] in hmap_s:
                if hmap_s[s[i]] != t[i]:
                    return False
                    
            if t[i] in hmap_t:
                if hmap_t[t[i]] != s[i]:
                    return False

            else:
                hmap_s[s[i]] = t[i]
                hmap_t[t[i]] = s[i]

        return True

        