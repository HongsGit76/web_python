def solution(n):
    answer = []
    while n>0:
        answer.append(n%10)  # 맨 뒷 자릿수 배열의 뒤에 추가하기
        n //= 10  # n을 10으로 나눈 몫을 n에 대입하기
    return answer