from heapq import heappop, heappush
from collections import defaultdict

INF = float('inf')

def solve():
    query = int(input())
    
    max_heap = []
    min_heap = []
    visited = defaultdict(int) # value가 0이면 추가한 만큼 뺀거고,
                               # 0이 아니면 아직 heap에서 사용해야된다
    
    for _ in range(query):
        cmd, n = input().split()
        n = int(n)
        if cmd == 'I':
            visited[n] += 1
            heappush(max_heap, -n)
            heappush(min_heap, n)
            
        else:
            if n == 1:
                while max_heap:
                    k = -heappop(max_heap)
                    if visited[k] > 0:
                        visited[k] -= 1
                        break
            else:
                while min_heap:
                    k = heappop(min_heap)
                    if visited[k] > 0:
                        visited[k] -= 1
                        break
    k,j = -INF,INF
    while max_heap and (k:=-heappop(max_heap)) < INF:
        if visited[k] > 0:
            break
        k = -INF
    while min_heap and -INF < (j:=heappop(min_heap)):
        if visited[j] > 0:
            break
        j = INF

    if -INF<k and j<INF:
        print(k,j)
    else:
        print("EMPTY")
    
    
tc = int(input())
for _ in range(tc):
    solve()