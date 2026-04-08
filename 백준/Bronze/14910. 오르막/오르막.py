seq = list(map(int, input().split()))

def check(arr):
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            return 0
    return 1

print("Good" if check(seq) else "Bad")