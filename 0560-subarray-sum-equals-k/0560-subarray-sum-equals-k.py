class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
                       0 1 2
        Input: nums = [1,1,1], k = 2
                           i

        res = max(res, curr - k if found) = max(1, 1)
        curr = 3 ; 3 - 2 = 1
        hmap = { # prefixsum: count
            0: 1
            1: 1

        }

        """

        hmap = {0: 1}
        res = 0
        curr_sum = 0

        for num in nums:
            curr_sum += num

            diff = curr_sum - k

            res += hmap.get(diff, 0)

            hmap[curr_sum] = 1 + hmap.get(curr_sum, 0)

        return res