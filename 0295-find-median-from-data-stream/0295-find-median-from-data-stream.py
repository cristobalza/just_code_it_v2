class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, -1* num)
        # make sure that every num in minheap is < than maxheap
        if self.minheap and self.maxheap and (-1*self.maxheap[0] > self.minheap[0]):
            val =-1 * heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, val)
        # same size?
        if len(self.minheap) > len(self.maxheap) + 1:
            val = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -1 * val)
        if len(self.maxheap) > len(self.minheap) + 1:
            val = -1 * heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, val)

    def findMedian(self) -> float:
        # 3 cases: 1,2) if one of the heaps is larger, return the root 1 or 2 
        #          3) if both heaps have same size, return (root1 + root2) / 2
        if len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        elif len(self.maxheap) > len(self.minheap):
            return -1 * self.maxheap[0]
        else:
            return (self.minheap[0] + -1 * self.maxheap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
