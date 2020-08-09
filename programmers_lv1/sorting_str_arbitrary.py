def solution(strings, n):
    hash = {}
    for s in strings:
        hash[s[n]] = s
    sorted = list(hash.keys())
    sorted.sort()
    print(sorted)
    return True
    

strings_1 = ["sun", "bed", "car"]
strings_2 = ["abce", "abcd", "cdx"]
print(solution(strings_2, 2))
