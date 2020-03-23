# 시도 방법

- stack 자료구조 사용

# 해결 방법

- 해결방법

  1. arrangement 배열을 돌며 괄호가 여는건지('(') 닫는건지(')') 검사한다.
  2. 여는 것 이라면 stack에 추가
  3. 닫는 것이라면, stack을 일단 pop()하고 현재까지 stack에 추가 된 여는 괄호의 갯수를 answer에 더한다.
  4. 단, 닫는 괄호가 이어질 경우에는 answer += 1을 한다.(Laser가 나가지는 않고, 막대기가 끊어지는 부분)

  

  ```python
  def solution(arrangement): answer = 0
  	stack = []
    for i, a in enumerate(arrangement):
        if a == '(':
            stack.append('(')
        elif a == ')':
            stack.pop()
            if arrangement[i-1] == '(':
                answer += len(stack)
            else:
                answer += 1
    
    return answer
  ```

  

# 어려웠던 부분

- 한번 풀어 본 문제다 보니 쉽게 풀었당

