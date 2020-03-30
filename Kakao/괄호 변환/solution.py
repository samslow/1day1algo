def stackCheck(str):
    stack = []
    if len(str) == 0:
        return True
    for ss in str:
        if ss == "(":
            stack.append("(")
        elif ss == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
                
    return True

def flipBracket(brackets):
    result = []
    for bracket in brackets:
        if bracket == "(":
            result.append(")")
        elif bracket == ")":
            result.append("(")
            
    return "".join(result)
    
def devide(w):
    result = ["",""]
    left, right = 0, 0
    
    for ww in w:
        print("ww", ww, left, right, result)
        if(left*right > 0 and left == right):
            result[1] = w[left+right:]
            break
        result[0] += ww
        if ww == "(" : left +=1
        else: right += 1
        
    return result
    
def convert(s):
    if stackCheck(s) == True:
        return s
    else:
        devided = devide(s)
        if stackCheck(devided[0]) == True:
            return devided[0] + convert(devided[1])
        else:
            u_inverted = flipBracket(devided[0])
            
            return "(" + convert(devided[1]) + ")" + u_inverted[1:-1]

def solution(p):
    answer = convert(p)
    
    return answer