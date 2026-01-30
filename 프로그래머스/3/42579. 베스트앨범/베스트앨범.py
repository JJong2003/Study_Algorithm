def solution(genres, plays):
    set_genres = set(genres)
    dict_genres = {genre:0 for genre in list(set_genres)}
    
    for i in range(len(plays)):
        dict_genres[genres[i]] += plays[i]
    
    infos = [(genres[i], plays[i], i) for i in range(len(plays))]
    infos.sort(key=lambda x : (-x[1], x[0]))
    print(infos)
    ans = []
    print(dict_genres)
    
    new_dict = {}
    
        
    while dict_genres:
        M = max(dict_genres, key=dict_genres.get)
        dict_genres.pop(M)
        
        cnt = 0
        for i in range(len(infos)):
            if infos[i][0] == M:
                cnt += 1
                ans += [infos[i][2]]
                if cnt == 2:
                    break
    return ans
                
    
        