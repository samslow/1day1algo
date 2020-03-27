# 총평

- DP
- 그림을 그려서 접근하니까 생각보다 금방 풀렸다.
- 처음에는 DP문제의 특징인 끝에서 처음으로를 생각했는데, 다시 생각 해 보니 어차피 위에있는 값이 더해지면서 내려오는거니까 처음부터 내려와도 되겠다고 생각함.
- DP문제처럼 기본 dictionary를 정의하지 않고도 할 수 있음
- 이보다 더 쉽게는 못 할듯 처음보다는 많이 줄인 코드양

# 해결 방법

- 해결 순서

  1. triangle의 1번째 인덱스부터 선택 가능한 i-1의 인덱스의 값을 마지막 인덱스까지 더한다.
  2. triangle의 마지막 인덱스에서 max 값 출력

  ```python
  def solution(triangle):
      for i in range(1, len(triangle)):
          for j in range(i+1):
              if j == 0:
                  triangle[i][0] += triangle[i-1][0]
              elif j == i:
                  triangle[i][i] += triangle[i-1][i-1]
              else:
                  if triangle[i-1][j-1] >= triangle[i-1][j]:
                      triangle[i][j] += triangle[i-1][j-1]
                  elif triangle[i-1][j-1] < triangle[i-1][j]:
                      triangle[i][j] += triangle[i-1][j]
                      
      return max(triangle[-1])
  ```

  