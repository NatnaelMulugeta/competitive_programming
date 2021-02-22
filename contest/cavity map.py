def cavityMap(grid):
    for i, row in enumerate(grid[1:-1], 1):
        for j, cavity in enumerate(row[1:-1], 1):
            
            neighbours = [grid[i+1][j], row[j+1], grid[i-1][j], row[j-1]]
            valid = True
            
            for cell in neighbours:
                if cavity > cell:
                    continue
                else:
                    valid = False
                    
            if valid:
                row = row[:j] + 'X' + row[j+1 : len(row)]
        
        grid[i] = row

    return grid