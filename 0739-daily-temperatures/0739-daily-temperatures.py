class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        temperatures = [73,74,75,71,69,72,76,73]
                                       i
        
        stack [(75, 2),]
        res [1,1,0,0,1,0,0]

        while stack and stack[-1][0] < temp[i]
            stack_t, stack_i = stack.pop()
            res[stack_i] = i - stack_i
        
        stack.append((temp[i], i))

        """

        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                stack_t, stack_i = stack.pop()
                res[stack_i] = i - stack_i

            stack.append((temperatures[i], i))

        return res