from collections import deque
import sys
input = sys.stdin.readline

def D(num):
    return str((int(num) * 2) % 10000)


def S(num):
    return  str(int(num) - 1) if int(num) > 0 else '9999'


def L(num):
    num = num.zfill(4)
    return num[1] + num[2] + num[3] + num[0]


def R(num):
    num = num.zfill(4)
    return num[3] + num[0] + num[1] + num[2]


q = int(input())
ans = []
for _ in range(q):
    visited = [0] * 10001
    a, b = input().split()

    q = deque([(a, '')])
    while q:
        num, cmd = q.popleft()

        if int(num) == int(b):
            ans.append(cmd)
            break

        if visited[int(num)]:
            continue
        visited[int(num)] = 1
        q.append([D(num), cmd + 'D'])
        q.append([S(num), cmd + 'S'])
        q.append([L(num), cmd + 'L'])
        q.append([R(num), cmd + 'R'])
print('\n'.join(ans))