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
