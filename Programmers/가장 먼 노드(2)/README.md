# 시도 방법

- BFS

# 해결 방법

- 1트와 다른 점

  - 성능에 영향을 끼칠 정도는 아니지만, 전체적으로 불필요한 변수와 for-loop이 있었다.

  ```python
  def bfs(graph, n):
      queue = []
      distances = {i:0 for i in range(1, n+1)}
      
      queue.append(graph[1])
      depth = 1
      while queue:
          for _ in range(len(queue)):
              nodes = queue.pop(0)
              for node in nodes:
                  if distances[node] == 0:
                      queue.append(graph[node])
                      distances[node] = depth
          depth += 1
      # print("distances", distances)
      
      del distances[1]
      
      max_depth = max(distances.values())
      result = 0
      for k, v in distances.items():
          if v == max_depth:
              result += 1
      
      return result
  
  def solution(n, edge):
      answer = 0
      
      graph = {i: [] for i in range(1, n+1)}
      for (e1,e2) in edge:
          graph[e1].append(e2)
          graph[e2].append(e1)
      # print("graph", graph)
      
      answer = bfs(graph, n)
      
      return answer
  ```

  

# 어려웠던 부분

- 확실히 다시보니까 @진선 박 말대로 전형적인 bfs 문제인 듯.
- 바이블로 삼자.