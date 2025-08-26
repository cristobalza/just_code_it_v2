class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_dict = {0:1}
        curr = 0

        for num in nums:
            curr += num
            diff = curr - k

            res += prefix_dict.get(diff, 0)

            prefix_dict[curr] = 1 + prefix_dict.get(curr, 0)
        
        return res