def solution(s):
    string = s.lower()
    print(string)
    num_p = 0
    num_y = 0
    for i in string:
        if i == "p":
            num_p += 1
        elif i == "y":
            num_y += 1
    if num_p == num_y:
        return True
    else:
        return False

s = "pPopYooyY"
print(solution(s))