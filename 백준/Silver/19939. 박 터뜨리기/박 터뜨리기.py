b,t=map(int,input().split())
print(-1if-~t*t/2>b else t-1*(-~t*t/2%t==b%t))