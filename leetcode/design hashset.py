class MyHashSet:

    def __init__(self):
        # Initialize the data structure here
        self.hashset = dict()

    def add(self, key: int) -> None:
        if key not in self.hashset:
            self.hashset[key] = key

    def remove(self, key: int) -> None:
        if key in self.hashset:
            del self.hashset[key]

    def contains(self, key: int) -> bool:
        # Returns true if this set contains the specified element
        if key in self.hashset:
            return True
        
        return False
        

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)