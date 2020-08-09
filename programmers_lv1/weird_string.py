def solution(s):
    answer = ''
    sList = s.split(" ")  # 문자열을 단어로 나누기
    for word in sList:
        wordLength = len(word)
        answer += " "  # 단어간 공백 추가
        for i in range(wordLength):
            if i % 2 == 0:  # 짝수 인덱스 대문자 만들기
                answer += word[i].upper()
            else:  # 홀수 인덱스 소문자 만들기
                answer += word[i].lower()
    answer = answer[1:]
    return answer

s = "try hello world"
print(solution(s))

a= s[0].upper()
print(a)