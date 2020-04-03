def solution(routes):
    routes = sorted(routes)
    answer = 1
    temp = routes.pop(0)
    for r in routes:
        if max(r[0], temp[0]) <= min(r[1],temp[1]):
            temp = [max(r[0],temp[0]),min(r[1],temp[1])]
        else:
            temp = r
            answer += 1
    return answer