class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] # store (current, min_val)
        min_val = float("inf")

        for i, num in enumerate(nums):

            # pop values that <= new num (exclude the current or equal values to update the min_val)
            while stack and stack[-1][0] <= num:
                stack.pop()

            if stack and num > stack[-1][1]:
                return True

            min_val = min(min_val, num)
            stack.append((num, min_val))

        return False