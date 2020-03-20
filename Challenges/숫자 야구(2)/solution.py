    from itertools import permutations

    def check_challange(challange, shot):
        strike, ball = 0, 0
        
        for i in range(3):
            if challange[i] == shot[i]:
                strike += 1
            elif challange[i] in shot:
                ball += 1
                
        return (strike, ball)

    def solution(baseball):
        shots = []
        numbers = [str(num) for num in range(1, 10)]
        
        for s in permutations(numbers, 3):
            shots.append("".join(s))
        
        for (challange, strike, ball) in baseball:
            temp = []
            for shot in shots:
                if check_challange(str(challange), shot) == (strike, ball):
                    temp.append(shot)
            shots = temp
            print(shots)
        return len(shots)
