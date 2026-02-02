for i in range(3):
    num = input()
    try:
        num = int(num) + 3-i
        print( num if not (k:=('Fizz'*(num%3==0) + 'Buzz'*(num%5==0))) else k)
        break
    except:
        None