# 시도 방법

- 그래프 문제이기 떄문에 BFS or DFS 라고 생각했고
- 문제를 읽고 BFS라고 생각했다.

# 해결 방법

1. dictionary로 문제에서 주어진  edge를 활용해 graph를 저장하는 부분
2. 1번에서 만든 graph를 활용해 bfs로 각 노드까지의 거리를 저장하는 distances dictionary 찾는 부분
3. 2번에서 만든 distances로 값들의 최대 값을 찾아 해당 값을 가지는 노드 있으면 answer += 1
4. return

```python
def bfs(graph, n):
    queue, result= [], []
    distances = {i:0 for i in range(1, n+1)}
    
    queue.append(graph[1])
    
    distance = 1
    while queue:
        for _ in range(len(queue)):
            nodes = queue.pop(0)
            for node in nodes:
                if (distances[node] == 0):
                    distances[node] = distance

                    routes = []
                    for edge in graph[node]:
                        routes.append(edge)
                    queue.append(routes)
        distance += 1
        
    del distances[1]
            
    return distances;
    

def solution(n, edge):
    answer = 0
    graph = {}
    # BFS Search를 시도
    for e in edge:
        if e[0] in graph:
            graph[e[0]].append(e[1])
        else:
            graph[e[0]] = [e[1]]
        if e[1] in graph:
            graph[e[1]].append(e[0])
        else:
            graph[e[1]] = [e[0]]
    
    distance_max = max(bfs(graph, n).values())
    for value in bfs(graph, n).values():
        if value == distance_max:
            answer += 1
    
            
    return answer
```



# 어려웠던 부분

- 바로 전 타겟넘버에서 DFS에 익숙 해 지며 BFS도 단순히 큐를 사용하는거라 쉬울 줄 알았는데 거리계산 기능이 들어가서 생각을 조금 더 해야 했다.

- 다음 주에는 이런 문제를 더 풀어 봐야 할 듯. 재미있네

- 다른 사람 풀이를 보니 개선 가능했던 부분

  - graph dict 생성 간소화 → 사실 코드가 이쁘게 될 뿐 성능에는 영향 없음

    for (a, b) in edge: graph[a-1].append(b-1) graph[b-1].append(a-1)