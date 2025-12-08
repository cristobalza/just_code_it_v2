class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hmap = {}

        for num in nums2:
            while stack and stack[-1] < num:
                key_num = stack.pop()
                hmap[key_num] = num # this is next greater element (num) for key_num

            stack.append(num)

        return [hmap.get(num, -1) for num in nums1]


