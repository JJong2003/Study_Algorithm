from collections import deque

INF = float('inf')

D, N1, N2, C1, C2, Tc = map(int, input().split())
wash = [(N1, C1), (N2, C2)]
wash.sort(key = lambda x: (x[1], x[0]))

if wash[1][0] > wash[0][0] and wash[1][1] > wash[0][1]:
    wash.pop()

T = [int(input()) for _ in range(D)]
short_wash = min(N1, N2)

def cal_cost(toies):
    avail = toies
    can_wash = deque()
    cannot_wash = deque()
    ret = 0
    
    for i in range(D):
        while cannot_wash and cannot_wash[0][1] <= i - short_wash:
            can_wash.append(cannot_wash.popleft())
        
        avail -= T[i]
        if avail < 0:
            need = -avail
            avail = 0
            if not can_wash:
                return INF
            
            # 1. 저렴한 것
            # 2. 기간이 짧은 것    
            for k in range(2):
                if need <= 0:
                    break
                period, cost = wash[k]
                if k == 0:
                    # 앞에서부터 적은 코스트로 소독을 해
                    while can_wash and can_wash[0][1] <= i - period:
                        num, date = can_wash.popleft()

                        if need > num:
                            need -= num
                            ret += num*cost
                            continue
                        else:
                            tmp = [num - need, date]
                            ret += need*cost
                            can_wash.appendleft(tmp)
                            need = 0
                            break
                else:
                    #뒤에서부터 비싼 코스트로 소독을 해
                    while can_wash:
                        num, date = can_wash.pop()
                        if need > num:
                            need -= num
                            ret += num*cost
                            continue
                        else:
                            tmp = [num - need, date]
                            ret += need*cost
                            can_wash.append(tmp)
                            need = 0
                            break
            if need > 0:
                return INF
        tmp = [T[i], i]
        cannot_wash.append(tmp)

    return ret

def get_max_and_sum(_list):
    s, m = 0, 0
    for i in _list:
        s += i
        m = max(m, i)
    return (m, s)

l, r = get_max_and_sum(T)


# for i in range(l, r+1):
#     result = cal_cost(i)
#     print(i, ":",result, i*Tc, result+i*Tc)

save = dict()
while l+2<r:
    mid1 = l + (r-l)//3
    mid2 = r - (r-l)//3
    
    if mid1 in save:
        result1 = save[mid1]
    else:
        result1 = cal_cost(mid1) + mid1*Tc
        save[mid1] = result1
    
    if mid2 in save:
        result2 = save[mid2]
    else:
        result2 = cal_cost(mid2) + mid2*Tc
        save[mid2] = result2
    
    if result1 < result2:
        r = mid2
    else:
        l = mid1
    
ans = INF
for i in range(l, r+1):
    result = INF
    if i in save:
        result = save[i]
    else:
        result = cal_cost(i) + Tc*i
    ans = min(ans, result)
print(ans)