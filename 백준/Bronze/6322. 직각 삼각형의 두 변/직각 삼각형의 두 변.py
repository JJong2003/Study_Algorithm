i = 0
while (i:=i+1)>0:
    a, b, c = map(int, input().split())
    if a == 0 and b==0 and c==0:
        break
    print(f"Triangle #{i}")
    square = 0
    if a == -1:
        square = ((c**2 - b**2)**0.5)
        print("Impossible." if c <= b else"a = %.3f" %square)
    elif b == -1:
        square = ((c**2 - a**2)**0.5)
        print("Impossible." if c <= a else"b = %.3f" %square)
    else:
        square = ((a**2 + b**2)**0.5)
        print("c = %.3f" %square)
    print()