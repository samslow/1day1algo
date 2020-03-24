# 시도 방법

- Stack을 쓸 수 있을 것 같긴 한데, 일단은 그냥 완전탐색처럼 해봐야지

- 아 안되겠구나 ㅎ 처음과 그 다음까지는 가능한데, 3번째부터는 1번째 상태를 알 수 없기 때문에 stack이 나을듯

  ```python
  def solution(prices):
      retension, answer = [], []
      # retension = [0 for _ in range(len(prices))]
      
      while prices:
          price = prices.pop(0)
          count = 0
          for p in prices:
              if p >= price:
                  count += 1
              else:
                  count += 1
                  break
          retension.append(count)
      
      return retension
  ```

  

- 위에 처럼 하니까 정답은 다 맞는데, 효율성 테스트가 시간 초과가 남

- .... python의 문제가 이 문제에 있는 듯 하다. Stack으로 하니까 시간초과가 나지만 deque 자료구조로 푸니까 맞았다.

# 해결 방법

- 해결 순서

  1. prices를 FIFO로 사용하기 위해 deque로 추상화
  2. prices를 하나씩 보면서 count를 retension에 기록

  ```python
  from collections import deque
  
  def solution(prices):
      retension = []
      prices = deque(prices)
      
      while prices:
          price = prices.popleft()
          count = 0
          for p in prices:
              count += 1
              if p >= price:
                  continue
              else:
                  break
          retension.append(count)
      
      return retension
  ```

  

# 어려웠던 부분

- 문제 자체를 푸는데는 20분도 안 걸렸는데, 효율성을 고치는데 다시 20분이 걸렸다.