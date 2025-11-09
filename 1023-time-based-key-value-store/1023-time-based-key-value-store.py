class TimeMap:

    def __init__(self):
        self.hmap = {} # key: [value, timestamp]
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hmap:
            self.hmap[key] = []
        self.hmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmap:
            return ""

        res = ""
        value_time_list = self.hmap[key]
        l, r = 0, len(value_time_list) - 1

        while l <= r:
            m = (l + r) // 2

            if value_time_list[m][1] <= timestamp:
                res = value_time_list[m][0]
                l = m + 1
            else:
                r = m - 1

        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)