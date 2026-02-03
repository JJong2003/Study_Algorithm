isbn = input()
star_idx = -1
total = 0 #별표 제외

for i in range(12):
    if isbn[i] == '*':
        star_idx = i
    else:
        total += int(isbn[i]) * (3 if i%2 else 1)

if isbn[12] == '*':
    print((10 - total%10)%10)
else:
    check = int(isbn[12])
    target = (10 - check) % 10
    
    need = (10 - ((total + check) % 10)) % 10
    w = (3 if star_idx%2 else 1)
    
    for x in range(10):
        if (w * x) % 10 == need:
            print(x)
            break