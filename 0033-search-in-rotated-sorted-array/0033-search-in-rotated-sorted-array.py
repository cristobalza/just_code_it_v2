class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Input: nums = [5,6,0,1,2,3,4], target = 0
                       l           
                                   r
                             m
        check if one is right or left side is sorted
        then check if target is between that
        if not, go to the opposite side and do the same 
            since its rotated once, it will guarantee that at least one side is it (if exists)
            else return -1
        """

        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            
            # Check right side first
            if nums[m] <= nums[r]:
                if nums[m] < target and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            # If not, check left side
            else:
                if nums[l] <= target and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1 

        return -1
        