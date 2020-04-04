def solution(budgets, M):
    min_budget, max_budget = 0, max(budgets)
    answer = 0
    
    while min_budget <= max_budget:
        avg = (min_budget + max_budget) // 2
        restricted = [b if b < avg else avg for b in budgets]
        if sum(restricted) <= M:
            min_budget = avg + 1
            answer = avg
        elif sum(restricted) > M:
            max_budget = avg - 1
    
    return answer