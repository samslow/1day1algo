# 총평

- 완전 탐색인듯 DP인듯
- 소수 찾기는 에라토스테네스의 체를 이용

# 해결 방법

- 해결 순서와 해답 코드

  1. 에라토스테네스의 체를 이용해 배수들을 False로 처리함
  2. 남은 primes를 가지고 numbers의 순열이 그 안에 있는지 체크

  ```python
  from itertools import permutations
  
  def solution(numbers):
      n=1000000
      a = [False,False] + [True]*(n-1)
      primes=[]
      answer = set()
  
      for i in range(2,n+1):
          if a[i]:
              primes.append(i)
              for j in range(2*i, n+1, i):
                  a[j] = False
      for i in range(1, len(numbers)+1):
          permList = list(permutations(list(numbers), i))
          for perm in permList:
              num = int("".join(list(perm)))
              
              if num in primes:
                  answer.add(num)
  
      return len(answer)
  ```