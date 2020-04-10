# 총평

- 몰라서 검색함
- 학부때 배운 개념이었음.. 크루스칼과 프림 그리고 MST
- 크루스칼
  - 간선의 비용이 최대인 것부터 제외 해 보며 MST가 유지되는지 확인
- 프림
  - 간선의 비용이 최소인 것부터 추가 해 보며 MST가 만들어지는지 확인
- 사실 코드 자체를 간소화 하도록 쓸 수도 있는데, 이번 기회에 kruskal 배워보려고 기능 함수로 분리함
- 이런 류의 MST 문제는 무조건 크루스칼과 프림을 써서 DFS로 순환하며 그리디 서치하는 패턴이다.

# 해결 방법

- 해결 순서와 해답 코드

  1. graph로 모든 간선으로 가는 가중치 배열을 만든다.
  2. 가중치와 시작, 종료 노드가 있는 edges를 만든다.
  3. 크루스칼 알고리즘으로 MST graph를 만든다.
     1. heap정렬로 가중치 높은 순으로 정렬하고
     2. 엣지의 수가 노드의 수보다 1개 적을때까지 loop돌며 가중치 큰 것부터 제외 해 간다.
     3. 만약 간선을 제거했는데 Tree가 모두 연결 되지 않으면 그 edge는 다시 되돌리고 다음 edge로 넘어간다.
  4. 0번 노드부터 연결된 간선끼리 dfs로 돌며 가중치들을 모두 더한 값을 리턴한다.

  ```python
  import heapq
  
  def is_connect(n, graph, is_visit, here, dest):
      if is_visit[here]:
          return False
      if here == dest:
          return True
      
      res = False
      is_visit[here] = True
      
      for to in range(n):
          if graph[here][to] > 0 and is_visit[to] == False:
              res |= is_connect(n, graph, is_visit, to, dest)
          
      return res
  
  def kruskal(n, edges, graph):
      pq = []
      edge_count = 0
      
      for edge in edges:
          w, v, u = edge
          heapq.heappush(pq, (-w, v, u))
          edge_count += 1
      
      while edge_count >= n:
          w, v, u = heapq.heappop(pq)
          graph[v][u] = 0
          graph[u][v] = 0
          edge_count -= 1
          is_visit = [False] * n
          
          if not is_connect(n, graph, is_visit, v, u):
              edge_count += 1
              graph[v][u] = -w
              graph[u][v] = -w
      
      return graph
  
  def dfs(n, graph, is_visit, here):
      if is_visit[here] == True:
          return 0
      
      is_visit[here] = True
      res = 0
      
      for there in range(n):
          if graph[here][there] > 0 and not is_visit[there]:
              res += graph[here][there]
              res += dfs(n, graph, is_visit, there)
              
      return res
      
              
  def solution(n, costs):
      edges = [ (w, v, u) for (v, u, w) in costs ] 
      graph = [ [0] * n for _ in range(n) ]
      
      for (w, v, u) in edges:
          graph[v][u] = w
          graph[u][v] = w
          
      graph = kruskal(n, edges, graph)
      
      is_visit = [False] * n
      answer = dfs(n, graph, is_visit, 0)
      
      return answer
  ```

  