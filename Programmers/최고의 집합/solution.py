def solution(n, s):
    standard = s // n
    if standard < 1: return [-1]
    answer = [standard] * n
    
    for i in range(s % n):
        answer[-i-1] += 1
    
    return answer