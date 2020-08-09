def solution(s, n):
    answer = ""
    upper_AL = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lower_al = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for al in s:
        if al is " ":
            answer+=" "
        elif al.islower():
            idx = lower_al.index(al)
            if idx + n > 25:
                answer+= lower_al[idx+n-26]
            else:
                answer += lower_al[idx+n]
        else:
            idx = upper_AL.index(al)
            if idx + n > 25:
                answer+= upper_AL[idx+n-26]
            else:
                answer += upper_AL[idx+n]
    return answer

print(solution("z",1))