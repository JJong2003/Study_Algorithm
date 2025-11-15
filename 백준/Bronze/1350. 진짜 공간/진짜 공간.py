import math

n = int(input())
files = list(map(int, input().split()))
cluster = int(input())

ans = 0
for i in range(n):
    if files[i] == 0: continue
    if cluster < files[i]:
        ans += math.ceil(files[i]/cluster) * cluster
    else:
        ans += cluster

print(ans)
