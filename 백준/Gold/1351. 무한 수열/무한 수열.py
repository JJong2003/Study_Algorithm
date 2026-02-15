N,P,Q = map(int, input().split())
seq = dict()
seq[0] = 1

def dp(i):
    if i in seq:
        return seq[i]
    seq[i] = dp(i//P) + dp(i//Q)
    return seq[i]

if __name__ == '__main__':
    print(dp(N))