class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = collections.Counter(nums)
        maxheap = []
        for num, freq in count_dict.items():
            heapq.heappush(maxheap, (-freq, num))
        
        res = []
        while k > 0:
            _, num = heapq.heappop(maxheap)
            res.append(num)
            k -= 1
        return res