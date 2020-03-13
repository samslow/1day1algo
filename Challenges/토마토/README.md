# 시도 방법

- 뭔가 형식적인 방법을 쓴 건가 싶긴 한데 굳이 썼다면 BFS
  - 주변 토마토가 익을 때마다 날짜를 하루씩 늘려가는 방식이므로
- 토마토가 앞뒤좌우로 익어가는식으로 농장을 끝까지 돌고나서 days return

# 해결 방법

- 해결 순서

  1. 표준 입력 받고 M, N, box를 세팅
  2. solution에 전달 해 주기 전에 토마토가 익을 수 있는지 검사
     1. 아예 하루도 익을 수 없으면 0
     2. 익은 토마토가 없으면 -1
  3. solution 함수에서 [앞, 뒤, 좌, 우]로 토마토를 익힘
  4. stack(tomatos)에 넣어서 (그렇다고 DFS는 아님) 비워 질 때마다 days +=1
  5. 익지않은 토마토가 0개면 days 리턴

  ```python
  def solution(farm, tomatos, tcount, utcount):
      # print("args: ", farm, tomatos, tcount, utcount)
      dx = [0, 0, 1, -1]
      dy = [1, -1, 0, 0]
  
      days = 0
      next_tomatos = tomatos[:]
      while next_tomatos:
          next_tomatos = []
          days += 1
          while tomatos:
              # print("tomatos: ", tomatos, "days: ", days)
              tomato = tomatos.pop()
              x, y = tomato
              for i in range(4):
                  move_x = x + dx[i]
                  move_y = y + dy[i]
                  if move_x >= N or move_y >= M or move_x < 0 or move_y < 0:
                      continue
                  point = farm[move_x][move_y]
                  if point == 0:
                      utcount -= 1
                      if utcount == 0:
                          return days
                      farm[move_x][move_y] = 1
                      next_tomatos.append([move_x, move_y])
          # print("next_tomatos", next_tomatos)
          tomatos = next_tomatos[:]
  
      return -1
  
  
  if __name__ == "__main__":
      # print("M과 N 입력")
      M, N = map(int, input().strip().split())
      # M, N = 2, 2
      box = []
      tomato = []
      tomato_count = 0
      untomato_count = 0
      empty_count = 0
      for i in range(N):
          # print("%s행 중 %s번째 줄 입력" % (str(N), str(i+1)))
          box.append(list(map(int, input().strip().split())))
      # box = [[1, -1], [-1, 1]]
  
      for i in range(N):
          for j in range(M):
              if box[i][j] == 1:
                  tomato_count += 1
                  tomato.append([i, j])
              elif box[i][j] == 0:
                  untomato_count += 1
              elif box[i][j] == -1:
                  empty_count += 1
      # print("result: ", end='')
      if tomato_count+empty_count == (M*N):
          print(0)
      elif tomato_count == 0:
          print(-1)
      else:
          print(solution(box, tomato, tomato_count, untomato_count))
  ```

  

![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/a93e9a75-548f-412b-aa25-fece42f2e329/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAT73L2G45EPETAT7P%2F20200313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200313T160133Z&X-Amz-Expires=86400&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF4aCXVzLXdlc3QtMiJIMEYCIQDnYOgTG8Ptu1Qvu0Qkbz2AEbXUUiGXhtg9w%2Bgk2zZ6qQIhAL8BuQ7WO4UKT3P%2BEuCOO%2BF0L%2FA4nKNe%2BSJ7Cmwm6YhYKrQDCEcQABoMMjc0NTY3MTQ5MzcwIgwWDo6TLcjPJargkQYqkQOKfgyShExn4U5b2ia1KXtW1nsGurhlAtr1h6mH8JcU4iWUcI3aObS8Q6fdOmO57bQO%2BPQibn3UDjH6C7ZJwljMfIL5vYiiUn6eqAkBVzxpLXQTXKfccMwqTlJgsvIrcpsdLWkGXeFH%2BJXPDxzBPfHeGaSIi5P5buUoQbzHTHS5n0un5KVNNp2aUocG9LFWkk8poMKfdipyMbNtks2SiffgbOu01kN2xeRl%2FQGKZM9SuLFqrf3bthK6ijXMlqaZ7rbEGM6ldEuH%2B5OkQnkUf5Dw%2FE4bczgCDdFyEXAUIMSDOr4zzI6hIbTSmT1trLlWjjtLZKSjKe66bsXipfpIdvxcjeir2s1yXQsQK40V5KQ75YJHpQ2%2Fk%2BtJUQ38COOraiRAhxm18kL2Jq%2FlubC8m8HJUO58vh2gpv4%2BawIUDT0O%2FEFVi%2BBn8%2F7V5JFH5ZCW53BjK5EHfU%2FftbnqFJvW%2Fx9kq%2FHtM%2FKTtSsvvAsHcH%2B20Q8Oql7MJKYTbEk7fxYLLMMgCHj4s4Zh%2B393LmnRR9M0BzCGoq7zBTrqAZMj6gwKsT8epLATptuumCG%2B3rF9ZrjxSeNla98FyBxafywxVsIOUH58peIz2pFK0rM5rmgWZPJxLgmyNakS%2BMFnktomtyGIPl%2FEhljOf%2B8BfBdgsWKR9qiV3vTNmNuiaIawSIkzBEQASa5QAdTDxv2fhmzzFP0gx1WRZypO2uG2bnQthTujC9aCpLiyQ0RUvdDDICoTllwBhrD7tHzf9ynhdltCsw6x8RUdIsRWRHikjg2qtL94NKpyzL46J4Y7mntAS5yZUA633VSpT8ECKxwjxbUaqboWlydQgQtc93lUJu%2BMIYPF%2B3CdLg%3D%3D&X-Amz-Signature=64cbd98ad5cd33ff9c702da32a6c28ae4adc494e605e05ec35bfdad61a7a324e&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

# 어려웠던 부분

- 2중 배열로 farm을 셋업하다보니 좌표가 헷갈렸음
- 시뮬레이션 조타