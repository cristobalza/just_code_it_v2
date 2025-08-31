class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hmap = collections.Counter(nums)

        max_freq = max(hmap.values())

        for num, freq in hmap.items():
            if freq == max_freq:
                return num