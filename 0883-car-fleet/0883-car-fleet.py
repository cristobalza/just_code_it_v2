class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        position = [10,8,0,5,3], speed = [2,4,1,1,3]
                     i
        
        [(10,2) (8,4) (0, 1) (5, 1) (3, 3)]

        sort(key=x : lambda x[0]) [(0, 1) (3, 3) (5, 1) (8,4) (10,2)]

        sort(reverse=True)  [(10,2) (0, 1) (3, 3) (5, 1) (8,4)]


Calculating the time for a car to reach the target is straightforward and can be done using the formula: 
time = (target - position) / speed


        10 - 10 / 2 = 0

        10 - 0 / 1 = 10
        """

        pos_speed_list = [(pos, sp) for pos, sp in zip(position, speed)]
        pos_speed_list.sort(key=lambda x: x[0], reverse=True)
        stack = []
        
        for pos, sp in pos_speed_list:
            time = (target - pos) / sp
            stack.append(time)

            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()

        return len(stack)



        