class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = collections.defaultdict(list)
        for word in strs:
            mask_arr = [0] * 26
            for ch in word:
                mask_arr[ord(ch) - ord("a")] += 1
            hmap[tuple(mask_arr)].append(word)
        return list(hmap.values())
