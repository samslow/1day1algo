# 총평

- 힙 자료구조

# 해결 방법

- 해결 순서와 해답 코드

  1. dates 중 stock이 0이 되기 전 날들의 supplies들을 힙에 넣는다.
     1. 이때, orient를 활용하여 공급이 필요한 또다른 날에 여러번 넣는다.
  2. 그중 가장 높은 supplies 부터 stock에 더해주며 k보다 stock이 커지는 날까지 loop
     1. loop마다 answer += 1
  3. answer 리턴

  ```python
  import heapq
  
  def solution(stock, dates, supplies, k):
      answer, orient = 0, 0
      plan = []
      
      while stock < k:
          for i in range(orient, len(dates)):
              if stock < dates[i]:
                  break
              heapq.heappush(plan, -supplies[i])
              orient += 1
          
          answer += 1
          stock -= heapq.heappop(plan)
      
      return answer
  ```