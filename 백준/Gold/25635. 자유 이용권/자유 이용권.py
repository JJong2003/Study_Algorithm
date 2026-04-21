n = int(input())
arr = list(map(int, input().split()))
M, S = 0, 0
for i in range(n):
    if arr[i] > M:
        M = arr[i]
    S += arr[i]

R = S - M
if M - R <= 1:
    print(S)
else: #if M - R >= 2:
    print(S - (M - R) + 1)
