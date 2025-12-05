import heapq

n = int(input())
works = [tuple(map(int, input().split())) for _ in range(n)]
works.sort(key=lambda x:(-x[0], x[1]))

classroom = [0]    # end time만 기록
cnt = 0
while works:
    s, e = works.pop()

    if classroom[0] <= s:    # 제일 일찍 끝나는 강의시간과 비교
                             # 이 시간보다 같거나 늦은 시간에 시작하는 강의는 강의실 재사용 가능
        heapq.heappop(classroom)
    heapq.heappush(classroom, e)

print(len(classroom))