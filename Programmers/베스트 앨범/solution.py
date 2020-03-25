def solution(genres, plays):
    answer = []
    ranking, genre_rank, comb = [], {}, {}
    for i, genre in enumerate(genres):
        if genre in genre_rank:
            genre_rank[genre] += plays[i]
        else:
            genre_rank[genre] = plays[i]
    print(genre_rank)
    genre_rank = sorted(genre_rank.items(), key=lambda e:e[1],reverse=True)
    for rank in genre_rank:
        ranking.append(rank[0])
    
    for i, t in enumerate(zip(genres, plays)):
        if t[0] in comb:
            comb[t[0]].append((i, t[1]))
        else:
            comb[t[0]] = [(i, t[1])]
    
    for c in comb.keys():
        comb[c] = sorted(comb[c], key=lambda e: e[1], reverse=True)
    print(comb)
    
    for genre in ranking:
        for c in comb[genre][:2]:
            answer.append(c[0])
    
    return answer