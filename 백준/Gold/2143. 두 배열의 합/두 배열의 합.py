from bisect import bisect_left, bisect_right

#입력
T = int(input())

n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

# prefix sum
pre_A = [0]
for i in range(n):
    pre_A.append(pre_A[i] + A[i])

pre_B = [0]
for i in range(m):
    pre_B.append(pre_B[i] + B[i])

# 부분합 모두 구하기
partitions_A = []
for i in range(len(pre_A)):
    for j in range(i+1, len(pre_A)):
        if i == j: continue
        partitions_A.append(pre_A[j] - pre_A[i])

partitions_B = []
for i in range(len(pre_B)):
    for j in range(i+1, len(pre_B)):
        if i == j: continue
        partitions_B.append(pre_B[j] - pre_B[i])
partitions_B.sort() #이분탐색 할 수 있게 정렬

# 정답 구하기
cnt = 0
for i in range(len(partitions_A)):
    partition = T - partitions_A[i] # 이 값을 찾을 것임
    
    left = bisect_left(partitions_B, partition)
    if left >= len(partitions_B):
        continue
    
    right = bisect_right(partitions_B, partition) - 1

    if partitions_B[left] == partition:
        cnt += right - left + 1
print(cnt)