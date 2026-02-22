Xc = []
Yc = []
for _ in range(int(input())):
  X, Y = map(int,input().split())
  Xc.append(X)
  Yc.append(Y)
Xc.sort()
Yc.sort()
print((Xc[-1]-Xc[0])*(Yc[-1]-Yc[0]))