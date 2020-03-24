# 시도 방법

- 처음에는 단순비교로 해 보려다가 실패..
- 다시한번 정석대로 BFS를 시도

# 해결 방법

- solution 함수 외에 `diff_only_one` 함수를 두어 각 글자가 1글자씩 만 다른지 체크함

- 한글자씩만 다르다면 compare 배열에 넣는다.

- words가 있는 동안 compare 배열에 target이 있는지 비교해보고

  - 있으면 return answer
  - 없으면 다음으로 진행(이때 Count가 하나씩 올라가야한다.)

  ```python
  def diff_only_one(x, y):
      count = 0
      for a, b in zip(x, y):
          if a is not b:
              count += 1
      
      return True if count is 1 else False
  
  def solution(begin, target, words):
      answer = 0
      stack = [begin]
      if target not in words:
          return 0
      while(words):
          print(stack)
          compare = []
          for s in stack:
              for i, w in enumerate(words):
                  if diff_only_one(s,w) is True:
                      compare.append(words.pop(i))
              print("compare", compare)
          answer += 1
          if target in compare:
              return answer
          else:
              stack = compare
      
      return answer
  ```

  

# 어려웠던 부분

- 역시 알고리즘 문제는 뻘짓이지!
- 2중 for-loop이 들어가면서 점점 헷갈리기 시작하는데, 변수 이름을 잘 지어야 될 것 같다.