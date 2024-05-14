from itertools import combinations

def solution(number):
    cnt = 0
    for a in combinations(number, 3):
        if sum(a) == 0:
            cnt += 1
    return cnt