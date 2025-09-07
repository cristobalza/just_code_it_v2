class Solution:
    def isHappy(self, n: int) -> bool:

        def helper(num):
            if num == 1:
                return True

            if num in hs:
                return False

            hs.add(num)

            total = 0

            while num > 0:
                total = total + (num % 10)**2

                num = num // 10

            return helper(total)

        hs = set()
        return helper(n)



        
        