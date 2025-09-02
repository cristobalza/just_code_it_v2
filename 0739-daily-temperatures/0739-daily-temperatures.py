class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Input: temperatures = [73,74,75,71,69,72,76,73]
                               i
                                  j
                                      k

        use a stack
        store values in stack
        pop them if prev temp < curr temp
        save in the prev idx the difference 
        """
        n = len(temperatures)

        res = [0] * n

        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                prev_temp, idx = stack.pop()
                res[idx] = i - idx
            
            stack.append((temp, i))
        
        return res





        # res = [0] * n
        # for i in range(n):
        #     curr_temp = temperatures[i]

        #     for j in range(i + 1, n):
        #         next_temp = temperatures[j]
        #         if next_temp - curr_temp > 0:
        #             res[i] = j - i
        #             break

        # return res
        