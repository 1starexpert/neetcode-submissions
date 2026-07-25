class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        We use a heap/ priority queue to easily grab the
        two largest stones each time
        """
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        # all stones added
        print(heap)
        while len(heap) > 1:
            
            stone_x = heapq.heappop(heap)
            stone_y = heapq.heappop(heap)
            if stone_x < stone_y:
                heapq.heappush(heap, stone_x - stone_y)
            if stone_y < stone_x:
                heapq.heappush(heap, stone_y - stone_x)
            print(heap)
        if len(heap) == 0:
            return 0
        return -heap[0]

        