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