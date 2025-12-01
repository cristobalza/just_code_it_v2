class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last_i = len(nums) - 1
        res = 0 # k
        i = 0

        while i <= last_i:
            if nums[i] != val:
                i += 1
                res += 1
            else:
                # swap with the last one 
                nums[i], nums[last_i] = nums[last_i], nums[i]

                # move last_i to the left
                last_i -= 1

        return res


        