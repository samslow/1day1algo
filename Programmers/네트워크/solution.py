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
