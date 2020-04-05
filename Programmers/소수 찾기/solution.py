from itertools import permutations

def solution(numbers):
    n=1000000
    a = [False,False] + [True]*(n-1)
    primes=[]
    answer = set()

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    for i in range(1, len(numbers)+1):
        permList = list(permutations(list(numbers), i))
        for perm in permList:
            num = int("".join(list(perm)))
            
            if num in primes:
                answer.add(num)

    return len(answer)