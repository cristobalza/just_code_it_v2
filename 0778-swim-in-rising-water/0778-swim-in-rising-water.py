class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Custom Dijkstra
        ROWS, COLS = len(grid), len(grid[0])
        minheap = []    
        minheap.append((grid[0][0], 0, 0)) # (time, r, c)
        visited = set()

        while minheap:
            curr_time, r, c = heapq.heappop(minheap)
            
            if (r, c) in visited:
                continue
            
            visited.add((r, c))

            if r == ROWS - 1 and c == COLS - 1:
                return curr_time

            for _r, _c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= _r < ROWS and 0 <= _c < COLS and (_r, _c) not in visited:
                    max_t = max(curr_time, grid[_r][_c])
                    heapq.heappush(minheap, (max_t, _r, _c))
            
