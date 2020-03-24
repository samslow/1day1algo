# 시도 방법

- DP
- 1트와 다르게 풀어보려고 해보려고 중복제거쪽을 좀 파 봤는데, 결국 똑같더라

# 해결 방법

```
def solution(N, number):
    answer = -1
    dp = [set() for _ in range(8)]
    for i, v in enumerate(dp, start = 1):
        v.add(int(str(N) * i))
    
    for i in range(1, 8):
        for j in range(i):
            for op1 in dp[j]:
                for op2 in dp[i-j-1]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 / op2)
        # print(dp)
        if number in dp[i]:
            return i+1
    
    return answer
```

# 어려웠던 부분

- dp는 어렵다. 어려우니까 다시 해 봐야한다.
- 문제 접근하는 방법을 익혀야 할 듯.
- DP는 무조건 처음에 판을 깔고 시작한다(dp 배열)
  - 여기서 dp 배열 원소는 위에서는 set()을 사용했지만, 때에 따라선 0이 될 수도있고, True False가 될 수도 있다.