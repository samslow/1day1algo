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