# 총평

- 처음에는 브루트포스로 하나씩 값을 깎아가면서 했더니 정확성 굿 효율성 망
- 이분 탐색으로 푸는법을 구글링 해 봄

# 해결 방법

- 해결 순서와 해답 코드

  ```python
  def solution(budgets, M):
      min_budget, max_budget = 0, max(budgets)
      answer = 0
      
      while min_budget <= max_budget:
          avg = (min_budget + max_budget) // 2
          restricted = [b if b < avg else avg for b in budgets]
          if sum(restricted) <= M:
              min_budget = avg + 1
              answer = avg
          elif sum(restricted) > M:
              max_budget = avg - 1
      
      return answer	
  ```