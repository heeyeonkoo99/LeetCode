class TimeMap:

    def __init__(self):
        self.map=collections.defaultdict(list)
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        for i in range(len(self.map[key])-1,-1,-1):
            t,v=self.map[key][i]
            if t<=timestamp:
                return v
        return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)