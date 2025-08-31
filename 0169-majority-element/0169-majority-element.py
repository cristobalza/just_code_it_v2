class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hmap = {}
        max_freq = 0

        for num in nums:
            hmap[num] = 1 + hmap.get(num, 0)
            max_freq = max(max_freq, hmap[num])
        
        for num, freq in hmap.items():
            if freq == max_freq:
                return num