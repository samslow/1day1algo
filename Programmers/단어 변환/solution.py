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
