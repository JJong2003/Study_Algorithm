from collections import deque
from itertools import permutations

damage = [9, 3, 1]
used = set()

def sol():
    N = int(input())
    SCV = tuple(map(int, input().split()))

    q = deque()
    q.append((SCV, 0))

    while q:
        scvs, cnt = q.popleft()
        if scvs in used:
            continue
        used.add(scvs)
        if not list(filter(lambda x:x>0, scvs)):
            return cnt

        P = list(permutations(scvs))
        for i in range(len(P)):
            tmp = P[i]
            if len(tmp) == 3:
                k = (tmp[0] - 9, tmp[1] - 3, tmp[2] - 1)
            elif len(tmp) == 2:
                k = (tmp[0] - 9, tmp[1] - 3)
            else:
                k = (tmp[0] - 9, )
            q.append((k, cnt+1))

    return -1

if __name__ == '__main__':
    print(sol())
