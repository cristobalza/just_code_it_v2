class TimeMap:

    def __init__(self):
        self.hashmap = collections.defaultdict(list[tuple])

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        arr = self.hashmap.get(key, None)
        if arr is None:
            return ""
        
        if len(arr) == 0:
            return ""

        l, r = 0, len(arr)

        if arr[r - 1][0] <= timestamp: # get last one 
            return arr[r - 1][1]

        if arr[l][0] > timestamp: # timestamp is before the oldest timestamp
            return ""

        while l < r:
            mid = (l + r) // 2

            if arr[mid][0] <= timestamp:
                l = mid + 1
            else:
                r = mid

        return arr[r - 1][1]
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)