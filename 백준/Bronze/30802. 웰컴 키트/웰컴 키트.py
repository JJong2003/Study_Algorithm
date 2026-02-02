n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())

cnt = 0
for sz in size:
    cnt += sz//t + 1*(sz%t>0)
print(cnt)
print(n//p, n%p)