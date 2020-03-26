def connectedCount(type, n):
    result = []
    visited = {i:[] for i in range(1, n+1)}
    for i in range(1, n+1):
        stack = []
        stack.append(i)
        count = 0
        while stack:
            temp = stack.pop()
            if temp not in visited[i]:
                if temp != i: 
                    visited[i].append(temp)
                    count += 1
                stack.extend(type[temp])
        result.append(count)
        
    return result

def solution(n, results):
    answer = 0
    attacked = {i:[] for i in range(1, n+1)}
    attack = {i:[] for i in range(1, n+1)}
    
    for players in results:
        attacked[players[1]].append(players[0])
        attack[players[0]].append(players[1])
    print(attacked)
    print(attack)
    
    attacked_count = connectedCount(attacked, n)
    attack_count = connectedCount(attack, n)
    
    for i in range(n):
        if attacked_count[i] + attack_count[i] == n-1:
            answer +=1

    
    return answer