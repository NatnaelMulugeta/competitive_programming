class MyHashMap:

    def __init__(self):
        self.hashmap = dict()

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            del self.hashmap[key]
            self.hashmap[key] = value
        else:
            self.hashmap[key] = value
        

    def get(self, key: int) -> int:
        if key in self.hashmap:
            return self.hashmap[key]
        
        return -1

    def remove(self, key: int) -> None:
        if key in self.hashmap:
            del self.hashmap[key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)