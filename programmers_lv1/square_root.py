import math

def solution(n):
    x = 0
    b = False
    while x <= math.sqrt(n):
        if x == math.sqrt(n):
            answer = (x+1)**2
            b = True
            break
        x+=1
    if b is False:
        answer = -1
    
    return answer

print(solution(100000000000000))