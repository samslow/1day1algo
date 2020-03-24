# 시도 방법

- DP

# 해결 방법

- 1트와 다른 점
  - 다르지 않다. 중간에 if - else 문이 미세하게 다르긴 한데 알고리즘 자체는 같다.

```python
def solution(m, n, puddles):
    answer = 0
    dp = [[0]*(m+1) for _ in range(n+1)]
    print(dp)
    dp[1][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            elif [j,i] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    answer = dp[n][m] % 1000000007
    
    return answer
```



# 어려웠던 부분

- 이런 문제만 풀고 싶다.