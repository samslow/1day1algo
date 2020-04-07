# 총평

- 그냥 연습문제 수준이었음

# 해결 방법

- 해결 순서와 해답 코드

  1. 어차피 n x n input이므로 끝까지 가기 전에 잘라주면 index over 하지 않음
  2. 각 자리에 첫번째를 기준으로 합을 더해서 max 를 return

  ```python
  def hourglassSum(arr):
      sum_arr = []
      for i in range(len(arr)-2):
          for j in range(len(arr[i])-2):
              hg_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
              sum_arr.append(hg_sum)
          
      return max(sum_arr)
  ```

