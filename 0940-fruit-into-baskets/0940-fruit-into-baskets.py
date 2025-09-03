class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
                         0 1 2 3 4
        Input: fruits = [1,2,3,2,2]
                                 r
                           l
        
        tree type fruit[i]: count
        {
            1: 0 X
            2: 3
            3: 1
        }
        hmap[fruit[r]] = 1 + hmap.get(r, 0)
        curr_sum += 1
        if len(hmap) > 2:
            fruit[l] # 1
            hmap[fruit[l]] -= 1
            l += 1
            curr_sum -= 1

            if not hmap[fruit[l]]:
                hmap.pop(fruit[l])



        curr_sum = 4
        res = max(3, 4) = 4

        res = max(res, curr_sum)
        """

        hmap = {}
        l = 0
        res = 0
        curr_sum = 0

        for r in range(len(fruits)):
            hmap[fruits[r]] = 1 + hmap.get(fruits[r], 0)
            curr_sum += 1

            if len(hmap) > 2:
                tree_fruit = fruits[l]
                hmap[tree_fruit] -= 1
                l += 1
                curr_sum -= 1

                if not hmap[tree_fruit]: 
                    hmap.pop(tree_fruit)
            
            res = max(res, curr_sum)

        return res
        