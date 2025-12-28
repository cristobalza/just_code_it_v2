class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        """
        Given
            points
            k

        Rturn
            list of points of size of k that are closest to the origin 

        [[3,3],[5,-1],[-2,4]]

        euclidean_distance((0,0), [3,3]) -> sqrt(((0 - 3)**2) + ((0- 3)**2)) = 4.2

        euclidean_distance((0,0), [-2,4]) -> sqrt(((0 - -2)**2) + ((0- 4)**2)) = 4.2

        """
        from math import sqrt

        euclidean_distance = lambda p1, p2: sqrt(((p1[0] - p2[0])**2) + ((p1[1] - p2[1])**2))

        maxheap = []

        for x, y in points:

            heapq.heappush(maxheap, (-euclidean_distance((0, 0), (x, y)), (x, y)))

            if len(maxheap) > k:
                heapq.heappop(maxheap)

        return [point for _, point in maxheap]

        