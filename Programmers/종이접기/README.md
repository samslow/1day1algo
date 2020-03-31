# 총평

- 점화식 ?
- 뭔가를 썼다고 하기에 애매한데.. 규칙을 찾았다 해야하나.. 다덜 이 문제에 사용된 알고리즘은 뭐라고 생각하시나여..

# 해결 방법

- 해결 순서

  - 한번 접을 때 마다 (기존의 접힌 자국) + 0 + (기존 접힌 자국 Flip) 규칙 이용

    ```python
    def solution(n): paper = [[0]]
    	for i in range(1, n):
          temp = paper[i-1] + [0] + list(map(lambda e : e ^ 1, paper[i-1]))[::-1]
          paper.append(temp)
      
      return paper[-1]
    ```