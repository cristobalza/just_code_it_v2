class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hmap = collections.defaultdict(list)
        for word in strs:
            sublist = [0] * 26
            for c in word:
                sublist[ord(c) - ord("a")] += 1
            
            hmap[tuple(sublist)].append(word)

        return list(hmap.values())

        
        