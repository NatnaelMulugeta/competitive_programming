class Solution:
    def findCircleNum(self, isConnected: [[int]]) -> int:
        province_count = 0
        self.visited = set()
        
        for i in range(len(isConnected)):
            if i not in self.visited:
                self.province_dfs(i, isConnected)
                province_count += 1
                
        return province_count
        
        
    def province_dfs(self, i: int, isConnected: [[int]]):
        self.visited.add(i)
        for j in range(len(isConnected)):
            if j not in self.visited and i != j and isConnected[i][j] == 1:
                self.province_dfs(j, isConnected)
        
        return
            