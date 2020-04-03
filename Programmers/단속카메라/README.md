# 총평

- 그리디 알고리즘

# 해결 방법

- 해결 순서와 해답 코드

  1. routes 를 정렬하여 앞에서부터 겹치는거 순서대로 나열
  2. 카메라가 커버할 수 있는 범위를 좁혀가며 하나의 카메라로 커버하는 부분 설정하며 카메라 대수 증가

  ```python
  def solution(routes):
      routes = sorted(routes)
      answer = 1
      temp = routes.pop(0)
      for r in routes:
          if max(r[0], temp[0]) <= min(r[1],temp[1]):
              temp = [max(r[0],temp[0]),min(r[1],temp[1])]
          else:
              temp = r
              answer += 1
      return answer
  ```

  