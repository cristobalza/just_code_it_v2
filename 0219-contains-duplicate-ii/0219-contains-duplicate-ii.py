class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """

        nums = [1,2,3,1], k = 3
                i.    j

                3 - 0 = 3 <= k = 3

        hmap to store pairs of value: idx

        iterate through the array
            if num is in hmap
                if i - hmap[num] <= k
                    return True
            add values to the hmap

        return False

        """

        hmap = collections.defaultdict(int)

        for i, num in enumerate(nums):
            if num in hmap:
                if i - hmap[num] <= k:
                    return True
            hmap[num] = i
        
        return False