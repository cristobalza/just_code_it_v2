class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i]

        postfix = [1] * n
        postfix[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i]

        
        answer = []
        
        for i in range(n):
            prefix_val = prefix[i - 1] if i - 1 >= 0 else 1
            postfix_val = postfix[i + 1] if i + 1 < n else 1

            answer.append(prefix_val * postfix_val)
        
        return answer
        