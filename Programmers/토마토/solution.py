def solution(farm, tomatos, tcount, utcount):
    # print("args: ", farm, tomatos, tcount, utcount)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    days = 0
    next_tomatos = tomatos[:]
    while next_tomatos:
        next_tomatos = []
        days += 1
        while tomatos:
            # print("tomatos: ", tomatos, "days: ", days)
            tomato = tomatos.pop()
            x, y = tomato
            for i in range(4):
                move_x = x + dx[i]
                move_y = y + dy[i]
                if move_x >= N or move_y >= M or move_x < 0 or move_y < 0:
                    continue
                point = farm[move_x][move_y]
                if point == 0:
                    utcount -= 1
                    if utcount == 0:
                        return days
                    farm[move_x][move_y] = 1
                    next_tomatos.append([move_x, move_y])
        # print("next_tomatos", next_tomatos)
        tomatos = next_tomatos[:]

    return -1


if __name__ == "__main__":
    # print("M과 N 입력")
    M, N = map(int, input().strip().split())
    # M, N = 2, 2
    box = []
    tomato = []
    tomato_count = 0
    untomato_count = 0
    empty_count = 0
    for i in range(N):
        # print("%s행 중 %s번째 줄 입력" % (str(N), str(i+1)))
        box.append(list(map(int, input().strip().split())))
    # box = [[1, -1], [-1, 1]]

    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                tomato_count += 1
                tomato.append([i, j])
            elif box[i][j] == 0:
                untomato_count += 1
            elif box[i][j] == -1:
                empty_count += 1
    # print("result: ", end='')
    if tomato_count+empty_count == (M*N):
        print(0)
    elif tomato_count == 0:
        print(-1)
    else:
        print(solution(box, tomato, tomato_count, untomato_count))
