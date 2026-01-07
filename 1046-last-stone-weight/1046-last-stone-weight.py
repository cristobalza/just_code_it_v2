class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []

        for stone in stones:
            heapq.heappush(maxheap, -stone)

        while len(maxheap) >= 2:
            stone_1 = heapq.heappop(maxheap)
            stone_2 = heapq.heappop(maxheap)

            if stone_1 != stone_2:
                heapq.heappush(maxheap, stone_1 - stone_2) 

        return -1 * maxheap[0] if maxheap else 0