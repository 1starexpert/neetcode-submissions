class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        time in hours [6/2, 9/2, 10/1, 3/1]
        """
        arr = []
        for i in range(len(position)):
            tup = (position[i], speed[i])
            arr.append(tup)
        # [(position, speed), (position, speed)]
        # [(0,1) (1,2) (4,2) (7,1)]
        #     10     4.5    3   3
        arr.sort()
        stack = []
        for element in arr:
            stack.append(element)
        counter = 0
        
        while len(stack) != 0:
            counter += 1
            tup = stack.pop()
            print(tup)
            if len(stack) == 0: 
                break
            arrival_time = (target - tup[0]) / tup[1]

            arrival_time_2 = (target - stack[-1][0]) / stack[-1][1]
            while arrival_time_2 <= arrival_time and len(stack) > 0:
                stack.pop()
                if len(stack) == 0:
                    break
                arrival_time_2 = (target - stack[-1][0]) / stack[-1][1]
            
        return counter

           
                



            
        