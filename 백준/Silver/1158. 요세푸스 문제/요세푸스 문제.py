N, K = map(int, input().split())
arr = [i+1 for i in range(N)]
ans = []
idx = K-1
while arr:
    ans.append(str(arr.pop(idx)))
    if arr:
        idx = (idx+K-1) % len(arr)
print(f"<{', '.join(ans)}>")