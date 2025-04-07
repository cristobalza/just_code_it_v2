class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, -1 * num)

        if self.minheap and self.maxheap and ((-1 * self.maxheap[0]) > self.minheap[0]):
            pop_val = -1 * heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, pop_val)

        if len(self.maxheap) > len(self.minheap) + 1:
            pop_val = -1 * heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, pop_val)


        if len(self.minheap) > len(self.maxheap) + 1:
            pop_val = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -1 * pop_val)


        

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return -1 * self.maxheap[0]
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        else:
            return ((-1 * self.maxheap[0]) + self.minheap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()