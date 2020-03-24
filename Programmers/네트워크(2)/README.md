# 시도 방법

- DFS, but BFS 였어도 상관 없음. 이런걸 graph 문제로 정의하나 ?

# 해결 방법

- 해결 순서

  1. graph문제는 먼저 map을 준비하는 것으로 시작하는 것이 좋다.
  2. 이후엔 graph의 각 노드를 하나씩 방문하며 bfs or dfs를 순회하며 visit 을 리턴하도록.
  3. set로 중복 제거를 하면 그 길이가 정답이 된다.

  ```python
  def dfs(start, graph):
      stack, visit = [], []
      stack.append(start)
      
      while stack:
          top = stack.pop()
          if top not in visit:
              visit.append(top)
              stack.extend(graph[top])
              
      return tuple(sorted(visit))
  
  def solution(n, computers):
      # graph로 각 노드가 어떤 computer와 연결되어 있는지 기록
      # graph를 dfs/ bfs로 돌며 연결되어 있는 것 끼리 묶어서 정답 return
      graph = {com: [] for com in range(1, n+1)}
      
      for i, computer in enumerate(computers, start=1):
          for j, com in enumerate(computer, start=1):
              if i != j and com == 1:
                  graph[i].append(j)
      
      network = set()
      for node in graph:
          network.add(dfs(node, graph))
      
      return len(network)
  ```

  