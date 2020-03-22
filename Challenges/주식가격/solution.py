from collections import deque

def solution(prices):
    retension = []
    prices = deque(prices)
    
    while prices:
        price = prices.popleft()
        count = 0
        for p in prices:
            count += 1
            if p >= price:
                continue
            else:
                break
        retension.append(count)
    
    return retension
