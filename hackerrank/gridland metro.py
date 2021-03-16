def gridlandMetro(n, m, k, track):
    original = n * m
    lst = []
    
    for i in range(k):
        r, c1, c2 = track[i]
        
        visited = True
        for j in range(len(lst)):
            if lst[j][0] == r:

                if not(c2 < lst[j][1] or c1 > lst[j][2]):
                    if c1 < lst[j][1]: 
                        lst[j][1] = c1
                        
                    if lst[j][2] < c2: 
                        lst[j][2] = c2
                        
                elif (c2 < lst[j][1] or c1 > lst[j][2]):
                    lst.append([r, c1, c2])
                    
                visited = False
                
        if visited == True:
            lst.append([r, c1, c2])
            
    blocked = 0
    for i in range(len(lst)):
        blocked += lst[i][2] - lst[i][1] + 1
        
    return original - blocked