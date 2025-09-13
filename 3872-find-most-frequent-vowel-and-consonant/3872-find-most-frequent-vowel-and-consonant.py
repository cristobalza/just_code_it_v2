class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel_set = set(['a', 'e', 'i', 'o', 'u'])

        hmap_vowel, hmap_consonant = {}, {}

        max_vowel_freq, max_consonant_freq = 0, 0

        for ch in s:
            if ch in vowel_set:
                hmap_vowel[ch] = 1 + hmap_vowel.get(ch, 0)
                max_vowel_freq = max(max_vowel_freq, hmap_vowel[ch])
            else:
                hmap_consonant[ch] = 1 + hmap_consonant.get(ch, 0)
                max_consonant_freq = max(max_consonant_freq, hmap_consonant[ch])
        
        return max_vowel_freq + max_consonant_freq
        
