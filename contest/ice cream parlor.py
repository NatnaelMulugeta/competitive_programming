def icecreamParlor(m, arr):
    dict = {}
    for i, elem in enumerate(arr):
        if (m - elem) in dict:
            return sorted([dict[m-elem], i+1])
        dict[elem] = i + 1
        
    