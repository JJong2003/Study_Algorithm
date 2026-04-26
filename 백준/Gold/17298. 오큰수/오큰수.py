n = int(input())
seq = list(map(int, input().split()))

stack = []
ans = [-1] * n
for i in range(n-1, -1, -1):
    val = seq[i]

    while stack:
        peek = stack.pop()
        if val >= peek:
            continue
        else:
            ans[i] = peek
            stack.append(peek)
            break
    stack.append(val)
print(*ans)