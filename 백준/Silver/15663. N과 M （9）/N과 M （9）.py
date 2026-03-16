import sys
print = sys.stdout.write

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

did = {}
selected = set()

def btk(limit, ans=None):
    if ans is None:
        ans = []
    if len(ans) == limit:
        tmp = ' '.join(map(str, ans))
        if tmp in did:
            return
        did[tmp] = 1
        print(tmp+"\n")
        return
    for i in range(len(arr)):
        if i in selected:
            continue
        selected.add(i)
        ans.append(arr[i])
        btk(limit, ans)
        ans.pop()
        selected.discard(i)
    return


btk(m)
