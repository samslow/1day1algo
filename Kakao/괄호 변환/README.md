# 총평

- 한번 풀어 본 문제였당
- 딱히 어려운 문제가 아니었고, 문제에서 주어진 대로 그대로 구현하면 풀 수 있다.
  - 다만 코드가 길어져서 더 줄여도 좋을 듯.

# 해결 방법

- 괄호가 올바른 괄호문자열 인가? or 빈 문자열인가?

  - 둘 중 하나라도 해당하면 그대로 반환

- 그렇지 않다면

  - 균형잡힌 u, v로 분리 (u는 더이상 쪼갤 수 없는 상태로)
  - u가 올바른 괄호 문자열이면
    - u + convert(v)
  - 아니라면
    - u를 뒤집고 '(' + convert(v) + ')' + u_inverted[1:-1] 반환

  ```python
  def stackCheck(str):
      stack = []
      if len(str) == 0:
          return True
      for ss in str:
          if ss == "(":
              stack.append("(")
          elif ss == ")":
              if len(stack) == 0:
                  return False
              else:
                  stack.pop()
                  
      return True
  
  def flipBracket(brackets):
      result = []
      for bracket in brackets:
          if bracket == "(":
              result.append(")")
          elif bracket == ")":
              result.append("(")
              
      return "".join(result)
      
  def devide(w):
      result = ["",""]
      left, right = 0, 0
      
      for ww in w:
          print("ww", ww, left, right, result)
          if(left*right > 0 and left == right):
              result[1] = w[left+right:]
              break
          result[0] += ww
          if ww == "(" : left +=1
          else: right += 1
          
      return result
      
  def convert(s):
      if stackCheck(s) == True:
          return s
      else:
          devided = devide(s)
          if stackCheck(devided[0]) == True:
              return devided[0] + convert(devided[1])
          else:
              u_inverted = flipBracket(devided[0])
              
              return "(" + convert(devided[1]) + ")" + u_inverted[1:-1]
  
  def solution(p):
      answer = convert(p)
      
      return answer
  ```

  