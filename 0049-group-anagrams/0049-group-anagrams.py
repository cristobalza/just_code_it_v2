class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_map = {}

        for word in strs:
            mask_count_list = [0]*26

            for char in word:
                mask_count_list[ord(char) - ord("a")] += 1
            
            # Save
            if tuple(mask_count_list) in dict_map:
                dict_map[tuple(mask_count_list)].append(word)
            else:
                dict_map[tuple(mask_count_list)] = []
                dict_map[tuple(mask_count_list)].append(word)
        
        return list(dict_map.values())