def solution(weight):
    answer = 1
    weight = sorted(weight)
    
    for w in weight:
        if answer >= w:
            answer += w
    
    return answer