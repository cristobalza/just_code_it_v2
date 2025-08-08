class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create hmap -> ascii array: list of words
        hmap = collections.defaultdict(list)
        for word in strs:
            lst = [0] * 26
            for ch in word:
                lst[ord("a") - ord(ch)] += 1
            hmap[tuple(lst)].append(word)
        return list(hmap.values())
        