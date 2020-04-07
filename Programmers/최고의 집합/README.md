# 총평

- 규칙성을 이용

# 해결 방법

- 해결 순서와 해답 코드

  1. s를 n으로 나눈 몫이 나누어 떨어지지 않으면 결과에 +1씩을 해준다.

  ```python
  def solution(n, s):
      standard = s // n
      if standard < 1: return [-1]
      answer = [standard] * n
      
      for i in range(s % n):
          answer[-i-1] += 1
      
      return answer
  ```

