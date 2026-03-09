works = int(input())

task = []
for i in range(works):
  times, limit = map(int,input().split())
  task.append([times,limit])
    
task.sort(key = lambda x : (x[1], x[0]))

start = task[0][1] - task[0][0]
t = start

while t>=0:
  suc_all = True
  for i in range(works):
    if start + task[i][0] > task[i][1]:
      t -= 1
      start = t
      suc_all = False
      break;
    start += task[i][0]
  if suc_all:
    print(t)
    break

if t<0:
  print(-1)