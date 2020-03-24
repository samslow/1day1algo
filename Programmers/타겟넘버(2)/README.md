# 시도 방법

- DFS
- 처음 시도했던 방법을 보니 어거지로 푼 감이 있어서( nonlocal 사용 ) 정석대로 해보자는 생각으로 접근

# 해결 방법

- 1트와 다른 점

  - 1트에서는 함수가 nonlocal을 사용해 sideEffect를 냈다.
  - 이번에는 그 문제를 해결하기 위해 재귀함수였던 dfs 내에서 값을 리턴하도록 했다.

  ```python
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
  ```

# 어려웠던 부분

- 처음 시도했을때 60점만 맞았다. 이유는 모든 경우의 수를 체크하지 않아서.

  ```
    def dfs(numbers, target, index):
        correct = False
        result = 0
        if sum(numbers) == target:
            correct = True
    		elif(index < len(numbers)):
            positive = dfs(numbers, target, index + 1)
            numbers[index] *= -1
            nagative = dfs(numbers, target, index + 1)
            
            result = positive + nagative    
        
        return result if correct is False else 1 + result
    
    def solution(numbers, target):
        answer = dfs(numbers, target, 0)
        
        return answer
  ```

  - 이렇게 하면 dfs내의 처음 if 문에서 target이 맞을 경우 그 이후 경우의 수를 계산 하지 않는다
    - [-1, 1, 1, 1, 1]인 경우 [-1,-1, 1, 1, 1]을 검사하지 않는다.