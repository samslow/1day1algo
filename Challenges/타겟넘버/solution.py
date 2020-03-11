def solution(numbers, target):
    answer = 0
    
    def dfs(numbers, target, index):
        if index < len(numbers):
            numbers[index] *= 1
            dfs(numbers, target, index+1)
        
            numbers[index] *= -1
            dfs(numbers, target, index+1)
        elif sum(numbers) == target:
            nonlocal answer
            answer += 1
    
    dfs(numbers, target, 0)
    
    return answer
