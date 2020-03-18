# 시도 방법

- 완전탐색
- 레드타일이 가장 길었을때부터, 반씩 쌓으며 계산된 갈색 타일의 수가 주어진 갈색 타일의 수와 일치하면 리턴

# 해결 방법

- 해결 순서

  ```python
  def solution(brown, red):
      redWidth, redHeight = red, 1
      while redHeight <= redWidth:
          brownCount = (redWidth+2) * (redHeight+2) - red
          if brownCount == brown:
              return [redWidth+2, redHeight+2]
          redHeight += 1
          redWidth = red / redHeight
  ```

  

# 어려웠던 부분

- 문제가 금방 풀려서 Syntatic Sugar를 생각하지 않고 최대한 줄여보았다.
  - 더 줄일 수 있을 것 같으면 알려주세요.