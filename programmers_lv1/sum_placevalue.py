def solution(n):
    answer = 0
    while n>0:
        answer += n%10  # 자릿수 더하기
        n //= 10  # n을 10으로 나눈 몫을 n에 대입하기
    return answer

print(solution(123))