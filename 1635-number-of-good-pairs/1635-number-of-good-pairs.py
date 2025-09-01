class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hmap = collections.defaultdict(list) # num: list of idxs
        res = []
        
        for i, num in enumerate(nums):
            if num in hmap:
                for idx in hmap[num]:
                    res.append([idx, i])
            hmap[num].append(i)

        return len(res)
            
        