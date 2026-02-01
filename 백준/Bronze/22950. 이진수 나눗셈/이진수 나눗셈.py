n = int(input())
m = int(input(), 2)
k = int(input())
r = '1' + '0'*k
r = int(r, 2)
print("NO" if m%r else "YES")