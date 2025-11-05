import copy
from collections import deque
import itertools

def containZero(lab_map):
    for row in lab_map:
        for elem in row:
            if elem == 0:
                return False
    return True

# virus 위치 정보 파악하기
def getVirusCoordinate(lab_map):
    virus_coor = [] #바이러스 위치 정보 보관
    for i in range(N):
        for j in range(N):
            if lab_map[i][j] == '*':
                virus_coor.append((i, j))
    return virus_coor


if __name__ == '__main__':
    # 기본 입력
    N, M = map(int, input().split())
    lab_map = [list(map(int, input().split())) for _ in range(N)]

    # 안에 0이 있는지 확인
    if containZero(lab_map):
        print(0)
        exit(0)

    # 지도 변환
    for i in range(N):
        for j in range(N):
            if lab_map[i][j] == 1:
                lab_map[i][j] = '-'
            elif lab_map[i][j] == 2:
                lab_map[i][j] = '*'

    virus_coor = getVirusCoordinate(lab_map) # 바이러스 위치 정보 보관
    virus_comb_set = list(itertools.combinations(virus_coor, M)) # 활성화 바이러스의 조합
    dxys = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    results = set()
    for i in range(len(virus_comb_set)):
        q = deque()
        visited = [[False for _ in range(N)] for __ in range(N)]  # 방문 체크
        for y, x in virus_comb_set[i]:
            q.append((y, x, 0))  # y, x, 퍼뜨린 시간
            visited[y][x] = True

        # 깊은 복사
        copied = copy.deepcopy(lab_map)

        while q:
            y, x, move_cnt = q.popleft()

            for dy, dx in dxys:
                ny, nx = y+dy, x+dx
                if 0>ny or ny>=N or 0>nx or nx>=N or visited[ny][nx]: continue

                if copied[ny][nx] == 0:
                    copied[ny][nx] = move_cnt + 1
                    q.append((ny, nx, move_cnt+1))
                    visited[ny][nx] = True
                elif copied[ny][nx] == '*':
                    q.append((ny, nx, move_cnt + 1))
                    visited[ny][nx] = True

        # 0이 있으면 전부 퍼뜨리지 못한 것임
        success = True
        maxi = 0
        for row in copied:
            for elem in row:
                if elem == 0:
                    success = False
                elif elem != '*' and elem != '-':
                    maxi = max(maxi, elem)
        results.add(maxi if success else -1)

    # 정답 출력
    ans = 2500
    res_list = list(results)
    for i in range(len(results)):
        if res_list[i] != -1:
            ans = min(ans, res_list[i])
    print(ans if ans < 2500 else -1)
