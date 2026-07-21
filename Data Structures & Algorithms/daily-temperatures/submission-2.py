class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        [30, 38, 30, 36, 35, 40, 28]

        stack:
        [(5, 40), ]

        result array:
        [1,4,1,2,1,0,0]
        """
        stack = []
        results = []

        for i in range(len(temperatures)):
            results.append(0)

        for i, value in enumerate(temperatures):
            if len(stack) != 0: 
                while value > stack[-1][1]:
                    tup = stack.pop()
                    index = tup[0]
                    days = i - index
                    results[index] = days 

                    if len(stack) == 0:
                        break
            stack.append((i, value))
        return results



        