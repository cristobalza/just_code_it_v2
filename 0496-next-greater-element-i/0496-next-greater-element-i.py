class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_hmap = {num: -1 for i, num in enumerate(nums1)} # set all values to -1

        stack = [] # store value

        for _, num in enumerate(nums2):

            # pop the value < num (get next greater value)
            while stack and stack[-1] < num:
                stack_top = stack.pop()
                nums1_hmap[stack_top] = num

            stack.append(num)

        res = []
        for num in nums1:
            res.append(nums1_hmap[num])

        return res

        

        

         