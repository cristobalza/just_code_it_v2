class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:

        def lcm(a, b):
            return abs(a * b) // math.gcd(a, b)
        
        stack = []

        for num in nums:

            stack.append(num)

            while len(stack) >= 2 and math.gcd(stack[-2], stack[-1]) > 1:
                a = stack.pop()
                b = stack.pop()

                stack.append(lcm(a, b))

        return stack
                


        