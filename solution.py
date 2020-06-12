def solution(area):
    res = []
    while (area > 0):
        biggest_square_side = int(area ** 0.5)
        biggest_square = biggest_square_side ** 2
        area -= biggest_square
        res.append(biggest_square)
    return res


T = int(input())

for t in range(T):
    s = int(input())
    solution_in = [int(x) for x in input().split()]
    solution_my = solution(s)
    print("area: {}".format(s))
    print("solution_in: {}".format(solution_in))
    print("solution_my: {}".format(solution_my))
    print(len(solution_in) == len(solution_my) and all(map(lambda v: v in solution_in, solution_my)))
