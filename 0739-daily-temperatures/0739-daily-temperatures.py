class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = [] # store index values (number of days)
        res = [0] * n # store the diff in index (if any) default is 0

        for i, temp in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < temp:
                last_temp_idx = stack.pop()
                res[last_temp_idx] = i - last_temp_idx

            stack.append(i)

        return res