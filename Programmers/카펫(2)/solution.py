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
