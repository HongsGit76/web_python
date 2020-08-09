def solution(numbers, hand):
    answer = ''
    """
    거리표
        0 1 2 3 4 5 6 7 8 9 10 11

    0   0 4 3 4 3 2 3 2 1 2  1  1
    2   3 1 0 1 2 1 2 3 2 3  4  4
    5   2 2 1 2 1 0 1 2 1 2  3  3
    8   1 3 2 3 2 1 2 1 0 1  2  2

    """
    distance_list = {0:[0,4,3,4,3,2,3,2,1,2,1,1], 2:[3,1,0,1,2,1,2,3,2,3,4,4], 5:[2,2,1,2,1,0,1,2,1,2,3,3], 8:[1,3,2,3,2,1,2,1,0,1,2,2]}
    L_R = [10, 11]  # *:10, #:11 로 표현
    for n in numbers:
        if n in [1,4,7]:
            answer+="L"
            L_R[0] = n
        elif n in [3, 6, 9]:
            answer+="R"
            L_R[1] = n
        else:
            left = distance_list[n][L_R[0]]
            right = distance_list[n][L_R[1]]
            if left>right:
                answer+="R"
                L_R[1] = n
            elif left<right:
                answer+="L"
                L_R[0] = n
            else:
                if hand == "right":
                    answer+="R"
                    L_R[1] = n
                elif hand == "left":
                    answer+="L"
                    L_R[0] = n
    return answer

n = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
h = "right"
print(solution(n,h))



