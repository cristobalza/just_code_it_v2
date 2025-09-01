class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        use ord to get unicode number of a letter

        build hashmap st tuple(arraya of unicode values) : list of corresponding words

        [1,1,0,0,0] : bat

        [1,0,0,0,0] : [nat, tan]

        return the values of the hmap
        """

        hmap = collections.defaultdict(list)

        for word in strs:
            unicode_mask = [0]*26

            for ch in word:
                unicode_mask[ord(ch) - ord("a")] += 1

            hmap[tuple(unicode_mask)].append(word)

        return list(hmap.values())
        