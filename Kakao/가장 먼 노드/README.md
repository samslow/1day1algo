# 총평

- 매우 어려워서 답을 풀이 봄
- 풀이를 봐도 좌표 문제다보니 실수를 조금씩 하게 되어서 시간이 오래 걸림
- BFS를 할 줄 아는 것과, 실제 코드로 구현하는 것을 보는 것은 다르다.
- 단순 노드가 아니라, 로봇이 2 x 1 구조라서 bfs 검사를 2번 해야한다.

# 해결 방법

- 키포인트

  - 회전 할 때 해당 방향 두 자리에 1이 하나라도 있으면 회전이 아예 불가하다.

- 해결 순서

  1. 풀이 용이성을 위해 board의 상하좌우에 1을 넣은 padding_board를 만든다.
  2. 큐에 시작 위치 (1,1),(1,2)를 넣는다.
  3. visited로 방문 검사를 한다.
  4. 움직 일 수 있는 배열을 move()에 정의한다.
     1. move()는 현재 배치로 상하좌우 이동가능한 배열과
     2. 회전 가능한 배열을 리턴한다.
  5. 시작 위치를 기점으로 Queue를 돌며
     1. 도착지 인지 확인하여 현재까지의 time을 리턴한다.
     2. Queue를 leftpop하여 move()에서 다음 위치를 Queue에 넣는다.

  ```python
  from collections import deque
  
  def move(loc1, loc2, board):
      around = [(1,0), (0,1), (-1,0), (0,-1)]
      rotate = [1,-1]
      result = []
      
      for a in around:
          if board[loc1[0] + a[0]][loc1[1] + a[1]] == 0 and board[loc2[0] + a[0]][loc2[1] + a[1]] == 0:
              result.append({(loc1[0] + a[0], loc1[1] + a[1]), (loc2[0] + a[0], loc2[1] + a[1])})
      
      if loc1[0]==loc2[0]: # 가로로 회전 가능 한 경우
          for r in rotate:
              if board[loc1[0]+r][loc1[1]] == 0 and board[loc2[0]+r][loc2[1]] == 0:
                  result.append({(loc1[0]+r, loc1[1]), (loc1[0], loc1[1])})
                  result.append({(loc2[0]+r, loc2[1]), (loc2[0], loc2[1])})
      elif loc1[1]==loc2[1]: # 세로로 회전 가능 한 경우
          for r in rotate:
              if board[loc1[0]][loc1[1]+r] == 0 and board[loc2[0]][loc2[1]+r] == 0:
                  result.append({(loc1[0], loc1[1]), (loc1[0], loc1[1]+r)})
                  result.append({(loc2[0], loc2[1]), (loc2[0], loc2[1]+r)})
  
      return result
  
  def solution(board):
      size = len(board)
      
      # 1로 먼저 padding을 채워 계산하기 쉽게 하면서 로봇이 바깥으로 나가지 않도록 한다.
      padding_board = [[1 for i in range(size+2)] for i in range(size+2)]
      for i in range(size):
          for j in range(size):
              padding_board[i+1][j+1] = board[i][j]
      
      que = deque()
      visited = []
      
      que.append([{(1,1), (1,2)}, 0])
      visited.append({(1,1), (1,2)})
      
      while len(que) != 0:
          next_value = que.popleft()
          loc = list(next_value[0])
          time = next_value[1] + 1
          
          for m in move(loc[0], loc[1], padding_board):
              if (size, size) in m:
                  return time
              if m not in visited:
                  que.append([m, time])
                  visited.append(m)
                  
      return 0
  ```

  