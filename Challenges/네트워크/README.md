# 시도 방법

- graph문제의 대명사 '네트워크' 이기 때문에 DFS 아니면 BFS 였다.
- 방문한 노드끼리 묶어주는 거기 때문에 DFS
- set을 사용해서 중복 제거

# 해결 방법

- 해결 순서

  1. python dfs 함수를 따로 빼서 계산 용이하도록 한다.
  2. grpah를 node 갯수 만큼 초기화 한다.
  3. computers를 nested for loop을 돌며 graph를 만든다.
  4. graph의 연결 노드끼리 set시켜 중복을 제거한 networks를 만든다.
  5. networks list의 length를 리턴한다.

  ```python
  def dfs(graph, start_node):
      visit, stack = [], []
      
      stack.append(start_node)
      
      while stack:
          node = stack.pop()
          if node not in visit:
              visit.append(node)
              stack.extend(graph[node])
      
      return visit
  
  def solution(n, computers):
      answer = 0
      graph = {node: [] for node in range(n)}
      
      for i, computer in enumerate(computers):
          for j, com in enumerate(computer):
              if i != j and com == 1:
                  graph[i].append(j)
      print(graph)
      networks = []
      for node in graph:
          networks.append(sorted(dfs(graph, node)))
      print(networks)
      answer = len(list(set([tuple(network) for network in networks])))
      
      return answer
  ```

  

  

# 어려웠던 부분

- 저번주 DFS문제랑 또이또이 한 듯. 이젠 좀 익숙해져서 한번만 더 해 보면 될 듯
- list를 set 하려고 하니 unhashable error가 났다.
  - set의 key로는 string, numbers, tuples만 사용 가능하기 때문이다.
  - tuple로 한번 감싸서 다시 list로 묶어줬더니 해결됨
  - 어? list로 안 감싸줘도 set 자체의 length를 체크만 해도 정답으로 인정되는 거 보니 set도 len() 되는 듯