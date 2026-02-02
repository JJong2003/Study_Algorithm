N = int(input())
tops = list(map(int, input().split()))

stack = []
ans = [0] * N

for i in range(N-1, -1, -1):
    height = tops[i]
    
    if not stack or tops[stack[-1]] > height:
        stack.append(i)
        continue

    while stack and tops[stack[-1]] <= height:
        ans[stack.pop()] = i+1
    stack.append(i)

print(' '.join(map(str, ans)))