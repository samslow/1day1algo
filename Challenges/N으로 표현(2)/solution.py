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
