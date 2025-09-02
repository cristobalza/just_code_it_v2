class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def comparator(x, y):
            if x + y < y + x:
                return 1

            elif x + y > y + x:
                return -1

            else:
                return 0

        nums_str = [str(num) for num in nums]

        nums_str.sort(key=cmp_to_key(comparator))

        res = "".join(nums_str)

        return res if res[0] != "0" else "0"



