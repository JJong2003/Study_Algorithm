def compare(a, b):
    sa = str(a)
    sb = str(b)
    case_A = str(sa+sb)
    case_B = str(sb + sa)

    if case_A > case_B:
        return a, b
    return b, a

def sorting(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            bigger, smaller = compare(lst[i], lst[j])
            lst[i], lst[j] = bigger, smaller

if __name__ == '__main__' :
    n = int(input())
    seq = list(map(int, input().split()))
    sorting(seq)
    k = ''
    for num in seq:
        k += str(num)
    print(int(k))
