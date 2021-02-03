import heapq
def heapSort(nums):
    heap = []
    for i in nums:
        heapq.heappush(heap, i)
        
    print([heapq.heappop(heap) for i in range(len(heap))])


nums = input().strip().split()
lst = [int(x) for x in input().strip().split()]
heapSort(lst)