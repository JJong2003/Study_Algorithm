from decimal import Decimal

N = int(input())
mice = [list(map(int,input().split())) for _ in range(N)]

get_posit = lambda x, y, vx, vy, t : (Decimal(x+vx*t), Decimal(y+vy*t))

def cal_all_mice_posit(time): # time은 실수범위
    return [get_posit(*m, time) for m in mice]

def get_leng(positions):
    ret = -1
    for i in range(N):
        m1 = positions[i]
        for j in range(i+1, N):
            m2 = positions[j]
            ret = max(ret, abs(Decimal(m1[0] - m2[0])), abs(Decimal(m1[1] - m2[1])))
    return ret


ans = float('inf')
le, ri = 0, 2<<63
while le + Decimal(10e-20) < ri:
    t1 = Decimal(le + (ri-le)/3)
    t2 = Decimal(ri - (ri-le)/3)
    
    mp1 = cal_all_mice_posit(t1)
    mp2 = cal_all_mice_posit(t2)
    
    L1 = get_leng(mp1)
    L2 = get_leng(mp2)
    
    if L1 > L2: le = t1
    else: ri = t2
    
    ans = min(ans, L1, L2)
print(ans)