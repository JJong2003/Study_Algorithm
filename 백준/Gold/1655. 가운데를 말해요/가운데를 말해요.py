from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
max_heap = []
min_heap = []
results = []

for i in range(N):
    num = int(input())
    if len(max_heap) == len(min_heap):
        heappush(max_heap, -num)
    else:
        heappush(min_heap, num)
    if min_heap and -max_heap[0] > min_heap[0]:
        max_value = -heappop(max_heap)
        min_value = heappop(min_heap)
        
        heappush(max_heap, -min_value)
        heappush(min_heap, max_value)
    results.append(str(-max_heap[0]))
    
print('\n'.join(results))