def solution(s):
    return s.isnumeric() and (len(s) == 4 or len(s) == 6)

s = "a1234"
solution(s)