class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:

        def gcm(a, b):
            return math.gcd(a, b)

        def lcm(a, b):
            if a == 0 or b == 0:
                return 0  # LCM is 0 if either number is 0
            return abs(a * b) // math.gcd(a, b)

        check_gcm = lambda a, b: gcm(a, b) > 1
        
        stack = []

        for num in nums:

            stack.append(num)

            while len(stack) >= 2 and check_gcm(stack[-2], stack[-1]):
                a = stack.pop()
                b = stack.pop()

                stack.append(lcm(a, b))

        return stack
                


        