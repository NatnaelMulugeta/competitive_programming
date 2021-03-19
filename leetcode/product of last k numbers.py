class ProductOfNumbers:
    def __init__(self):
        self.product = 1
        self.data = []

    def add(self, num: int) -> None:
        if num == 0:
            self.product = 1
            self.data = []      
        else: 
            self.product *= num
            self.data.append(self.product)         

    def getProduct(self, k: int) -> int:
        if len(self.data) == k:
            return self.data[-1]
        if len(self.data) > k:
            return int(self.data[-1] / self.data[-1-k])
        else:
            return 0
            

        
            
        
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)