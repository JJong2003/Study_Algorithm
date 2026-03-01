N, L, D = map(int, input().split())
alarm = [0]*(N*L+(N-1)*5)
idx = 0
while idx < len(alarm):
    for i in range(idx, min(idx+L, len(alarm))):
        alarm[i] = 1
    idx += 5+L

bell = 0
while bell < len(alarm):
    if alarm[bell] == 0:
        break
    bell += D
    
print(bell)