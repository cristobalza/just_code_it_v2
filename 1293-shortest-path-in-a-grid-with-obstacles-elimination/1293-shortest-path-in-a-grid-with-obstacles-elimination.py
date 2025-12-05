class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        minheap = [(0, 0, 0, 0)] # dist, obstacles, r, c
        min_obstacles = {} # (r, c): obstacles
        ROWS, COLS = len(grid), len(grid[0])

        while minheap:
            dist, obstacles, r, c = heapq.heappop(minheap)

            if r == ROWS - 1 and c == COLS - 1:
                return dist

            if (r, c) in min_obstacles and min_obstacles[(r, c)] <= obstacles:
                continue

            min_obstacles[(r, c)] = obstacles

            for adj_r, adj_c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= adj_r < ROWS and 0 <= adj_c < COLS:
                    new_obstacles = grid[adj_r][adj_c] + obstacles
                    if new_obstacles <= k:
                        heapq.heappush(minheap, (dist + 1, new_obstacles, adj_r, adj_c))

        return -1

    
