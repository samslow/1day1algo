def solution(n): paper = [[0]]
    for i in range(1, n):
      temp = paper[i-1] + [0] + list(map(lambda e : e ^ 1, paper[i-1]))[::-1]
      paper.append(temp)
  
  return paper[-1]