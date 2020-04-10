def is_possible(mid, stones, k):
    now = -1
    for i, s in enumerate(stones):
        if s - mid >= 0:
            if i - now > k: return False
            now = i
    if len(stones) - now > k: return False
    else: return True

def solution(stones, k):
    answer = 0
    left, right = 0, 200000000
    while left <= right:
        mid = (left + right) //2
        if is_possible(mid, stones, k):
            answer = mid
            left = mid + 1
        else:
            right = mid -1
    
    return answer