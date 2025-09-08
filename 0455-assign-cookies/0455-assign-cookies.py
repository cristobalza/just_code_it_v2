class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        i -> is the findContentChildren

        g[i] is the minimum size of a cookie that the child will be content with

        s[j] is the size of a cookie

        We can assign tthe j cookie to i if s[j] >= g[i]

        Return: Number integer that maximize the number of content children 
        

        Input: g = [1,2,3], s = [1,1]
                    i
                                 j

        """

        g.sort()
        s.sort()

        i = j = 0

        while i < len(g):
            
            while j < len(s) and g[i] > s[j]:
                j += 1

            if j == len(s):
                break

            i += 1
            j += 1

        return i

        