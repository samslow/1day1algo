def solution(m, n, puddles):
answer = 0

dp = [[0]*(m+1) for i in range(n+1)]
dp[1][1] = 1;

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i == 1 and j == 1:
            continue
        if [j,i] not in puddles:
            dp[i][j] = dp[i-1][j] + dp[i][j-1];
        else:
            dp[i][j] = 0
print(dp[n][m])

answer = dp[n][m] % 1000000007

return answer
