from collections import defaultdict

class Solution:
    def rectangleArea(self, rectangles: [[int]]) -> int:
        result = 0
        mod = 10**9 + 7
        
        xs = set()
        ys = set()
        for x1, y1, x2, y2 in rectangles:
            
            # collect X cordinates
            xs.add(x1)
            xs.add(x2)
            
            # collect Y cordinates
            ys.add(y1)
            ys.add(y2)
        
        # maximum area coverage 
        total = [[False for _ in ys] for _ in xs]
        
        x_dic = defaultdict(int)
        y_dic = defaultdict(int)
        
        for i, val in enumerate(sorted(xs)): 
            x_dic[val] = i
        for i, val in enumerate(sorted(ys)): 
            y_dic[val] = i
        
        for x1, y1, x2, y2 in rectangles:
            for x in range(x_dic[x1], x_dic[x2]):
                for y in range(y_dic[y1], y_dic[y2]):
                    total[x][y] = True
                    
        print(total)
        
        set_x, set_y = sorted(xs), sorted(ys)
        for x, row in enumerate(total):
            for y, found in enumerate(row):
                
                if found: result += (set_x[x+1] - set_x[x]) * (set_y[y+1] - set_y[y])
        
        return result % mod