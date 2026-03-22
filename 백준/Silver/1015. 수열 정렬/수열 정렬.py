n = int(input())
seq = list(map(int, input().split()))
ans = [-1] * n

idx = 0
while (k:=min(seq)) < 1001:
    for i in range(n):
        if seq[i] == k:
            ans[i] = idx
            idx += 1
            seq[seq.index(k)] = 1001
            break
print(*ans)