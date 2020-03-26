# 총평

- graph와 stack 자료구조를 사용
- 다 풀고 다른 사람 풀이 보니 다들 나보다는 간결하게 한듯
  - 나도 줄임 포인트가 있을 것 같긴 함
    - 굳이 attack, attacked를 나눠서 할 필욘 없는 거

# 해결 방법

- attack과 attacked로 graph를 각각 만들고 1번부터 stack을 돌면서 graph를 만듬

- 각 인덱스(1~5)가 이긴 선수의 수 + 각 인덱스가 진 선수의 수 == n-1 이면 answer +=1

- 즉, 이기고 진 횟수가 전체 인원수-1 과 같으면 그 선수의 순위는 빼박 정해짐

  ```python
  def connectedCount(type, n):
      result = []
      visited = {i:[] for i in range(1, n+1)}
      for i in range(1, n+1):
          stack = []
          stack.append(i)
          count = 0
          while stack:
              temp = stack.pop()
              if temp not in visited[i]:
                  if temp != i: 
                      visited[i].append(temp)
                      count += 1
                  stack.extend(type[temp])
          result.append(count)
          
      return result
  
  def solution(n, results):
      answer = 0
      attacked = {i:[] for i in range(1, n+1)}
      attack = {i:[] for i in range(1, n+1)}
      
      for players in results:
          attacked[players[1]].append(players[0])
          attack[players[0]].append(players[1])
      print(attacked)
      print(attack)
      
      attacked_count = connectedCount(attacked, n)
      attack_count = connectedCount(attack, n)
      
      for i in range(n):
          if attacked_count[i] + attack_count[i] == n-1:
              answer +=1
  
      
      return answer
  ```

  