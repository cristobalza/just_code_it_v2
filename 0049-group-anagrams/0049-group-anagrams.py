class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = collections.defaultdict(list)
        for word in strs:
            arr = [0] * 26
            for letter in word:
                arr[ord(letter) - ord('a')] += 1
            hmap[tuple(arr)].append(word) 
        return list(hmap.values())
        