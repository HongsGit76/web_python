def solution(n, lost, reserve):
    for sup in reserve:
        if sup - 1 in lost:
            lost.remove(sup - 1)
        elif sup + 1 in lost:
            lost.remove(sup + 1)
        elif sup in lost:
            lost.remove(sup)
    answer = n - len(lost)
    return answer

n = 3
lost = [2,3]
reserve = [3]
print(solution(n, lost, reserve))
