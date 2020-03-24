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
