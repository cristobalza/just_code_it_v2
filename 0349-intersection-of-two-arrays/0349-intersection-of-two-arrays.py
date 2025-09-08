class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hs = set()

        for num in nums1:
            hs.add(num)

        res = []

        for num in nums2:
            if num in hs and num not in res:
                res.append(num)

        return res