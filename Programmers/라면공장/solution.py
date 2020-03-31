import heapq

def solution(stock, dates, supplies, k):
    answer, orient = 0, 0
    plan = []
    
    while stock < k:
        for i in range(orient, len(dates)):
            if stock < dates[i]:
                break
            heapq.heappush(plan, -supplies[i])
            orient += 1
        
        answer += 1
        stock -= heapq.heappop(plan)
    
    return answer