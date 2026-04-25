n = int(input())
stack = list(map(int, input().split()))
sub = []
ans = [0] * (n)
while stack:
    while sub:
        k, i = sub.pop()
        if k <= stack[-1]:
            # 좌표 정답 처리
            ans[i+1] = len(stack)
        else:
            sub.append((k, i))
            break
    sub.append((stack.pop(), len(stack)-1))
print(*ans)