class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        res = 0

        for num in hset:
            if num - 1 not in hset:
                curr_size = 1

                while num + curr_size in hset:
                    curr_size += 1

                res = max(res, curr_size)

        return res