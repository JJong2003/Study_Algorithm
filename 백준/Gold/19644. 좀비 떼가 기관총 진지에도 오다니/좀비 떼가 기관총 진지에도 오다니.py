L = int(input())
Ml, Mk = list(map(int, input().split()))
C = int(input())  #수류탄

zombies = [int(input()) for _ in range(L)]

prefix = [0]
for i in range(L):
    idx = max(0, i - Ml +1)
    dmg = (prefix[i] - prefix[idx] + 1) * Mk
    
    if zombies[i] > dmg:
        C -= 1
        prefix.append(prefix[-1])
    else:
        prefix.append(prefix[-1] +1)

print("NO" if C < 0 else "YES")