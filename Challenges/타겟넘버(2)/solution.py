def dfs(numbers, target, index):
    correct = False
    result = 0
    if(index < len(numbers)):
        positive = dfs(numbers, target, index + 1)
        numbers[index] *= -1
        nagative = dfs(numbers, target, index + 1)
        
        result = positive + nagative
    elif sum(numbers) == target:
        correct = True
        
    return result if correct is False else 1 + result

def solution(numbers, target):
    answer = dfs(numbers, target, 0)
    
    return answer
