from collections import deque

def move(loc1, loc2, board):
    around = [(1,0), (0,1), (-1,0), (0,-1)]
    rotate = [1,-1]
    result = []
    
    for a in around:
        if board[loc1[0] + a[0]][loc1[1] + a[1]] == 0 and board[loc2[0] + a[0]][loc2[1] + a[1]] == 0:
            result.append({(loc1[0] + a[0], loc1[1] + a[1]), (loc2[0] + a[0], loc2[1] + a[1])})
    
    if loc1[0]==loc2[0]: # 가로로 회전 가능 한 경우
        for r in rotate:
            if board[loc1[0]+r][loc1[1]] == 0 and board[loc2[0]+r][loc2[1]] == 0:
                result.append({(loc1[0]+r, loc1[1]), (loc1[0], loc1[1])})
                result.append({(loc2[0]+r, loc2[1]), (loc2[0], loc2[1])})
    elif loc1[1]==loc2[1]: # 세로로 회전 가능 한 경우
        for r in rotate:
            if board[loc1[0]][loc1[1]+r] == 0 and board[loc2[0]][loc2[1]+r] == 0:
                result.append({(loc1[0], loc1[1]), (loc1[0], loc1[1]+r)})
                result.append({(loc2[0], loc2[1]), (loc2[0], loc2[1]+r)})

    return result

def solution(board):
    size = len(board)
    
    # 1로 먼저 padding을 채워 계산하기 쉽게 하면서 로봇이 바깥으로 나가지 않도록 한다.
    padding_board = [[1 for i in range(size+2)] for i in range(size+2)]
    for i in range(size):
        for j in range(size):
            padding_board[i+1][j+1] = board[i][j]
    
    que = deque()
    visited = []
    
    que.append([{(1,1), (1,2)}, 0])
    visited.append({(1,1), (1,2)})
    
    while len(que) != 0:
        next_value = que.popleft()
        loc = list(next_value[0])
        time = next_value[1] + 1
        
        for m in move(loc[0], loc[1], padding_board):
            if (size, size) in m:
                return time
            if m not in visited:
                que.append([m, time])
                visited.append(m)
                
    return 0