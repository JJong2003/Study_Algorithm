se, ga = map(int, input().split())
blocks = list(map(int, input().split()))

LeftWall = blocks[0]
LeftWallIdx = 0
water = 0
if ga==1: print(0);exit(0)
RightWall = blocks[1]
RightWallIdx = 1
i = 0
while i < ga:
    i += 1
    if i == ga: break
    Wall = blocks[i]

    if RightWall <= Wall:
        RightWall = Wall
        RightWallIdx = i

    if LeftWall <= RightWall and LeftWallIdx < RightWallIdx:
        H = min(LeftWall, RightWall)
        for j in range(LeftWallIdx+1, RightWallIdx):
            water += H - blocks[j]

        LeftWall = RightWall
        LeftWallIdx = RightWallIdx
        if i != ga-1:
            RightWall = blocks[i+1]
            RightWallIdx = i+1
        continue

    if i == ga-1:
        H = min(LeftWall, RightWall)
        for j in range(LeftWallIdx + 1, RightWallIdx):
            water += H - blocks[j]

        LeftWallIdx, RightWallIdx = RightWallIdx, RightWallIdx+1
        if ga <= RightWallIdx: break
        LeftWall, RightWall = RightWall, blocks[RightWallIdx]

        i = RightWallIdx

print(water)