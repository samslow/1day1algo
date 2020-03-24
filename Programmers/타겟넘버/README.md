# 시도 방법

- DFS 문제인데, 마구잡이식으로 해 봤어서 이번 기회에 제대로 DFS 파보려고 함

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/51914073-7a45-4588-b3db-3820124dc619/Untitled.png](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F51914073-7a45-4588-b3db-3820124dc619%2FUntitled.png?table=block&id=a39775d1-4c3b-4f1f-86ff-562294eb0fce&width=1860&cache=v2)

- 학부 때 배웠는데, 그림을 보니까 기억난다
- 2가지 구현 방식
  1. 재귀 함수
  2. 스택 → 효율성은 높을 듯

# 해결 방법

- 전역변수로 answer를 둔다고 생각하고(global로 선언 금지, 헷갈림) 재귀를 돌며 각 상황마다 target이 같으면 answer + 1
- 사실 꼬리재귀로 return 값을 물고 올라오며 해주려고 했는데, 잘 안되서 그냥 전역변수 사용 (찜찜)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c3226c0e-6741-4847-a7a7-3c394aa4a447/Untitled.png](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fc3226c0e-6741-4847-a7a7-3c394aa4a447%2FUntitled.png?table=block&id=cb031576-c029-4061-be0a-212496db5dbc&width=1440&cache=v2c)

# 어려웠던 부분

- DFS를 안 쓰고도 풀라면 풀 수 있었을 것 같은데, 거의 처음으로 DFS를 써 봐서 많이 헤멤
- 여러가지 시도를 해보느라 시간을 많이 씀
- nonlocal이라는 명령어를 처음 써 봤는데 자주 쓰면 좋지는 않을 듯. 딱 이런 상황에서만.

# 완성 코드

```
def solution(numbers, target):
    answer = 0
    
    def dfs(numbers, target, index):
        if index < len(numbers):
            numbers[index] *= 1
            dfs(numbers, target, index+1)
        
            numbers[index] *= -1
            dfs(numbers, target, index+1)
        elif sum(numbers) == target:
            nonlocal answer
            answer += 1
    
    dfs(numbers, target, 0)
    
    return answer
```