import heapq as h
import bisect as b

heap = []

n = int(input())
for i in range(n):
    ops = list(map(int, input().split()))
    
    if ops[0] == 1:
        b.insort_right(heap, ops[1])
    elif ops[0] == 2:
        heap.remove(ops[1])
    elif ops[0] == 3:
        print(heap[0])