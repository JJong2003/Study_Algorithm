n = int(input())
cranes = list(map(int, input().split()))
cranes.sort(reverse = True)

m = int(input())
boxes = list(map(int, input().split()))
boxes.sort(reverse = True)

ans = 0
if cranes[0] < boxes[0]:
    ans -= 1
else:
    while boxes:
        for crane in cranes:
            for box in boxes:
                if crane >= box:
                    boxes.remove(box)
                    break
        ans += 1

print(ans)