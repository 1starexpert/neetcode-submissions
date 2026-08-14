class Solution:
    import heapq
    import math
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            p = math.sqrt((x ** 2) + (y ** 2))
            tup = (p, points[i])
            points[i] = tup
        heapq.heapify(points)
        res = []
        for i in range(k):
            tup = heapq.heappop(points)
            res.append(tup[1])
        return res



        