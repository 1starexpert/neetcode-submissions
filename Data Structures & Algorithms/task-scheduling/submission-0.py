class Solution:
    import heapq
    from collections import deque
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        [-3, -1, -1]

        """
        # 1. Count the number of different items:
        task_count = {}
        for t in tasks:
            if t in task_count:
                task_count[t] += 1
            else:
                task_count[t] = 1

        # 2. Add each into a priority queue:
        heap = []
        for key in task_count:
            heapq.heappush(heap, -task_count[key])
        
        # 3. Start enqueing:
        q = deque()
        time = 0


        while len(heap) > 0 or len(q) > 0:
            time += 1
            
            if heap:
                task = 1 + heapq.heappop(heap)
                if task:
                    q.append((task, time + n))
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        return time

            