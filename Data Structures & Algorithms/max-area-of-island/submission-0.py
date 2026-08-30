from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        row = len(grid)
        col = len(grid[0])
        visited = set()
        self.max_area = 0

        def bfs(r, c):
            area = 0
            q = deque()
            visited.add((r,c))
            q.append((r,c))
            directions = [[0,1], [0,-1], [1,0], [-1,0]]

            while q:
                r, c = q.popleft()
                area += 1
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (nc in range(col) and 
                        nr in range(row) and grid[nr][nc] == 1 and
                        (nr, nc) not in visited):
                        q.append((nr, nc))
                        visited.add((nr, nc))
                self.max_area = max(area, self.max_area)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r,c) not in visited:
                    bfs(r, c)
        
        return self.max_area