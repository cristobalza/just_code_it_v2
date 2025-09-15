class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        fruits := List[int] -> i := tree
                               fruits[i] := type of fruit 

        Rules:
            -  two baskets only -> can only hold one type of fruit per basket. No limit on amount of fruits
            -  Starting at any tree, myst pick one fruit from every tree

        Input: fruits = [1,2,1]
                         l
                             r

                    basket = {1: 2, 2: 1}

                    window = r - l + 1

        Input: fruits = [0,1,2,2]
                           l
                               r

            basket = [1, 2]

            res = 3

        [3,3,3,1,2,1,1,2,3,3,4]
               l
                         r

         basket= {1, 2}

         res = 5

        """

        l = 0
        basket = {} # use a hmap as tree fruit: frequency

        n = len(fruits)

        res = 0

        for r in range(n):
            basket[fruits[r]] = 1 + basket.get(fruits[r], 0)

            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if not basket[fruits[l]]:
                    del basket[fruits[l]]

                l += 1

            res = max(res, r - l + 1)

        return res


