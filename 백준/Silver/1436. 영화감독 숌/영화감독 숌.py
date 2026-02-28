numb = []
n=int(input())
    

idx = 666
while len(numb) < n:
    if str(idx).find('666') >= 0:
        numb.append(idx)
    idx += 1

print(numb[n-1])