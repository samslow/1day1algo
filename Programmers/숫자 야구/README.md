# 시도 방법

- 완전탐색
  - 모든 경우의 수를 따져보는 방법
- 숫자 야구의 개념을 이해하는데 시간이 좀 걸림
- 순열(permutations)를 이용하면 중복되지 않은 숫자 배열을 만들 수 있을 듯
  - 단 int로 하면 계산이 복잡해지므로 stirng으로 비교하는게 더 나음

# 해결 방법

- 해결 순서

  1. 1~9까지 숫자로 나열 ( 조건에 따라 0 이나 10은 제외)
  2. permutations(순열)로 3자리수까지의 경우의수(9*8*7)를 attend에 저장
  3. cal_result를 사용해 각 경우의 수가 문제의 strike, ball과 일치하면 attend에 추가하는식으로 문제의 challenge 검증
  4. 최종으로 남는 경우의수는 length로 출력

  ```python
  from itertools import permutations
  
  def cal_result(challenge, number):
      strike, ball = 0, 0
      
      for i in range(3):
          if challenge[i] == number[i]:
              strike += 1
          elif challenge[i] in number:
              ball += 1
      
      return (strike, ball)
  
  def solution(baseball):
      answer = 0
      numbers = [ str(num) for num in range(1,10)]
      attend = []
      for a in permutations(numbers, 3):
          attend.append("".join(a))
      
      for (challenge, strike, ball) in baseball:
          attend = list(filter(lambda number: cal_result(str(challenge), number) == (strike, ball), attend))
      
      answer = len(attend)
      
      return answer
  ```

# 어려웠던 부분

- 완전탐색 문제는 처음인데 앞으로 더 익숙 해 져야 할 듯