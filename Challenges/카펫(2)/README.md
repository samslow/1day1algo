# 시도 방법

- 점화식?

# 해결 방법

- 1트와 다른점은 없다.

  ```python
  def solution(brown, red):
      red_width = red
      red_height = 1
      while red_width >= red_height:
          print("width: ", red_width, "height", red_height)
          area = (red_width+2) * (red_height+2) -red
          if area == brown:
              return [red_width+2, red_height+2]
          red_height += 1
          red_width = red / red_height
  ```

  

# 어려웠던 부분

- width와 heigth를 점화식으로 끌어내는 부분에서 정확한 수치를 계산하지 못 한 점