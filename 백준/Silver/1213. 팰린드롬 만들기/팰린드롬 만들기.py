name = list(input())
name.sort()
leng = len(name)
ans = ['']*leng
idx_name, idx_ans = 0, 0
tmp = name[-1]
while 1:
    if idx_name + 1 >= leng:
        ans[idx_ans] = tmp
        break
    if name[idx_name] == name[idx_name+1]:
        ans[idx_ans] = name[idx_name]
        ans[-1-idx_ans] = name[idx_name+1]
        idx_name += 2
        idx_ans += 1
    else:
        tmp = name[idx_name]
        idx_name += 1

def check(s):
    for i in range(len(s)//2+1):
        if s[i] != s[-1-i]:
            return False
    return True
    
print(k if check((k:=''.join(ans))) and len(k) == leng else "I'm Sorry Hansoo")