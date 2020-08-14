def solution(str1, str2):
    n = 0
    parlist = []
    while n + 1 < len(str1):
        if str1[n].isalpha() and str1[n+1].isalpha():
            par_str1 = str1[n].lower()+str1[n+1].lower()
            print(par_str1)
            parlist.append(par_str1)
        n+=1
    print(parlist)
    set_str1 = len(parlist)
    k = 0
    intersec = 0
    compl = 0
    while k+1 < len(str2):
        if str2[k].isalpha() and str2[k+1].isalpha():
            par_str2 = str2[k].lower()+str2[k+1].lower()
            print(par_str2)
            if par_str2 in parlist:
                intersec += 1
                parlist.remove(par_str2)
            else:
                compl += 1
        k+=1
    print(f"{compl} {intersec}")
    if not set_str1+compl == 0 :
        return int(intersec/(set_str1+compl)*65536)
    else:
        return 65536

str1 = "aa1+aa2"
str2 = "AAAA12"
print(solution(str1, str2))