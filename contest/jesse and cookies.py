
import heapq as h

def cookies(k, A):
    ops = 0
    lst = []
    for i in A:
        h.heappush(lst, i)
    
    while len(lst)>1 and any(a<k for a in lst):
        ops += 1
        top = h.heappop(lst)
        prev = h.heappop(lst)
        h.heappush(lst, 2*prev+top)
    if all(a>=k for a in lst):
        return ops
    return -1
  