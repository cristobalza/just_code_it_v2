class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        Calculate each path from 0,0 to (rows-1, columns-1) 
        - Get the MAX abs diff between 2 cells
        - Store those values for EACH path
        - Return the MINIMUM among all thos MAX values

        Djikstra algo - to get path of each possible node from 0, 0

        for each path, get the max and compare with the res to get the min

        effort - max abs diff

        """
        ROWS, COLS = len(heights), len(heights[0])
        visited = set()

        minheap = [(0, 0, 0)] # effort (max abs diff), r, c

        while minheap:
            effort, r, c = heapq.heappop(minheap)

            # Guarantee minimum effort because we store only the max ones
            if r == ROWS - 1 and c == COLS - 1:
                return effort

            if (r, c) in visited:
                continue

            visited.add((r, c))

            for adj_r, adj_c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= adj_r < ROWS and 0 <= adj_c < COLS and (adj_r, adj_c) not in visited:
                    curr_effort = abs(heights[r][c] - heights[adj_r][adj_c])
                    max_effort = max(curr_effort, effort)

                    heapq.heappush(minheap, (max_effort, adj_r, adj_c))









