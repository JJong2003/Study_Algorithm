import sys
sys.setrecursionlimit(10**7)

def solution(begin, target, words):
    if target not in words:
        return 0
    answer = dfs(begin, target, words)
    return answer


def differ(str1, str2):
    cnt = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            cnt += 1
            if cnt > 1:
                break
    return cnt == 1

def dfs(now, target, words, depth=0):
    if now == target:
        return depth
    local = float('inf')
    for i in range(len(words)):
        wd = words[i]
        if wd == "": #visited
            continue
        if differ(now, wd):
            words[i] = ""
            local = min(local, dfs(wd, target, words, depth+1))
            words[i] = wd
    return local
    
    