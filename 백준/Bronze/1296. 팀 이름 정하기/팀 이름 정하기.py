yd = input()
ans = [-1, '']
repeat = int(input())
candidates = [input() for _ in range(repeat)]
candidates.sort()
for cand in candidates:
    cnts = []
    for k in 'LOVE':
        cnts.append(cand.count(k) + yd.count(k))
    score = 1
    for i in range(len(cnts)):
        for j in range(i + 1, len(cnts)):
            score *= cnts[i] + cnts[j]
    if ans[0] < score % 100:
        ans[0] = score % 100
        ans[1] = cand
print(ans[1])