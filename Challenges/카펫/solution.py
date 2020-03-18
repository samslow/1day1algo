def solution(brown, red):
redWidth, redHeight = red, 1
while redHeight <= redWidth:
    brownCount = (redWidth+2) * (redHeight+2) - red
    if brownCount == brown:
        return [redWidth+2, redHeight+2]
    redHeight += 1
    redWidth = red / redHeight
