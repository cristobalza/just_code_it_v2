class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        res = [-1] * n
        stack = [] # store monotone decreasing values

        for i in range(2 * (n - 1), -1, -1):
            curr = nums[i % n]

            # pop values that are <= curr (not useful as next greater)
            while stack and stack[-1] <= curr:
                stack.pop()

            # fill result only in the first pass
            if i < n:
                if stack:
                    res[i] = stack[-1]

            stack.append(curr)

        return res 