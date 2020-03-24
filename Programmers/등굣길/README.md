# 시도 방법

- 당연하게도 DP 라고 써 있으니까 일단 이 방법 시도
- 하지만, DP의 대한 개념은 전날의 DFS, BFS만큼이었기에 다른 기초 문제를 먼저 풀어보기로 함.
  - https://lee-seul.github.io/algorithm/2017/03/16/dynamic-programming.html
- DP의 기본 개념은 어쨋든 `계산 한 것을 다시 계산하지 않는다` 로 부터 오는 효율성 문제이다.
- 귀납법으로 dp[0]에서 부터 차근차근 쌓아 간 뒤 dp[n]의 경우의 수를 출력 해 주면 되는 패턴

# 해결 방법

목적지에 들어가는 경우의 수는 해당 위치로부터 위나 왼쪽이기 때문에 그 위치들까지 가능한 경우의 수를 합하면 현재 위치까지의 경우의 수가 나온다. 이를 거꾸로 (DP) 하다보면 결국 처음 위치(\[1][1]의 값은 늘 1)가 나온다.

그럼 거기서 부터 쌓고, 목적지의 값 출력 해주면 끝

- 배열은 n*m 으로 지도처럼 초기화 해준다.

- 처음 시작은 무조건 1

- 처음부터(\[1][1] 제외) 이전 값을 토대로 현재 값을 계산한다.

  - 단, 이때 puddles 에 있는 값이라면 0으로 한다.

- 모두 계산 한 뒤 dp\[n][m] 출력

  ```python
  def solution(m, n, puddles):
      answer = 0
      
      dp = [[0]*(m+1) for i in range(n+1)]
      dp[1][1] = 1;
      
      for i in range(1, n + 1):
          for j in range(1, m + 1):
              if i == 1 and j == 1:
                  continue
              if [j,i] not in puddles:
                  dp[i][j] = dp[i-1][j] + dp[i][j-1];
              else:
                  dp[i][j] = 0
      print(dp[n][m])
      
      answer = dp[n][m] % 1000000007
      
      return answer
  ```

# 어려웠던 부분

- (m,n) 같은 좌표 문제일 경우
  - 가로 세로의 좌표 값이 배열의 안쪽은 가로, 배열의 바깥쪽은 세로임을 기억하자 → 은근 실수 많이 함.
  - 시작점이 (0,0)이 아닌 (1,1) 인 경우 계산의 편의성을 위해 (m+1),(n+1)로 하면 좋다.
- js의 include() 가 python의 in 임