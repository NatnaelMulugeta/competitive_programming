class Solution:
    def canVisitAllRooms(self, rooms: [[int]]) -> bool:
        
        visited = set()
        visited.add(0)
        
        stack = [0]
        while stack:
            room = stack.pop()
            
            for neighbour in rooms[room]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append(neighbour)
                    
        for i in range(len(rooms)):
            if i not in visited: return False
            
        return True