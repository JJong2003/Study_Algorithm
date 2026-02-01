import heapq

n = int(input())
card = [int(input()) for _ in range(n)]
heapq.heapify(card)

ans = 0
while len(card) > 1:
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    
    ans += a+b
    heapq.heappush(card, a+b)
print(ans)
