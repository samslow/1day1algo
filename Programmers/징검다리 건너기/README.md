# 총평

- 이분탐색으로 O(nLogn)으로 효율성 검사 패스
- 이분탐색의 바이블 같은 문제인듯

# 해결 방법

- 해결 순서와 해답 코드

  1. while문을 돌며 left가 right보다 커질 때까지 loop
  2. is_possible()에서 현재 징검다리를 넘을 수 있는지 확인

  ```python
  def is_possible(mid, stones, k):
      now = -1
      for i, s in enumerate(stones):
          if s - mid >= 0:
              if i - now > k: return False
              now = i
      if len(stones) - now > k: return False
      else: return True
  
  def solution(stones, k):
      answer = 0
      left, right = 0, 200000000
      while left <= right:
          mid = (left + right) //2
          if is_possible(mid, stones, k):
              answer = mid
              left = mid + 1
          else:
              right = mid -1
      
      return answer
  ```

