# 시도 방법

- DP

# 해결 방법

- 해결 순서

  1. dp에 연속된 숫자가 최대 8까지 오므로 set()으로(중복 제거용) 템플릿 세팅
  2. 각 set()에 해당 인덱스+1개의 N 배치
  3. N을 n번 사용해서 만들 수 있는 수의 일반화 적용
  4. 그 n번안에 number가 있으면 index + 1 리턴
  5. 그렇지 않으면 그대로 -1 리턴

  

  ```python
  def solution(N, number):
      answer = -1
      
      dp = [set() for _ in range(8)]
      
      for i, x in enumerate(dp, start=1):
          x.add(int( str(N) * i))
      
      for i in range(1, 8):
          for j in range(i):
              for op1 in dp[j]:
                  for op2 in dp[i-j-1]:
                      dp[i].add(op1+op2)
                      dp[i].add(op1-op2)
                      dp[i].add(op1*op2)
                      if op2 != 0:
                          dp[i].add(op1//op2)
          print(dp)
          if number in dp[i]:
              answer = i + 1
              break
      
      
      return answer
  ```

# 어려웠던 부분

- 접해 본 DP중 가장 어려웠음
- 일반화 하는 과정이 쉽지 않아 답을 봄
- 다음에는 답 없이도 풀 수 있었으면