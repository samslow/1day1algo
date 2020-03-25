# 총평

- 해시 자료구조로 접근
- 푸는 방법을 제대로 이해하고 접근했는데, 테스트케이스는 다 맞는데 채점 케이스에서 계속 틀림
  - 처음에 장르를 랭킹 해 주던 코드가 제대로 소팅을 안 해주고 있었음

# 해결 방법

- 해결 순서와 해답 코드

  ```python
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
  ```

  