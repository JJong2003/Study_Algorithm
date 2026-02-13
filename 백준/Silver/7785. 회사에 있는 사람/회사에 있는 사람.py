n = int(input())
employees = set()
for _ in range(n):
    name, log = input().split()
    if log == 'enter':
        employees.add(name)
    else:
        if name in employees:
            employees.discard(name)

answer = list(employees)
answer.sort(reverse=True)
print('\n'.join(answer))