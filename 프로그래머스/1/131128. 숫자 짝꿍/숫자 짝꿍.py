from collections import Counter

def solution(X, Y):
    num = ''
    y_counter = Counter(Y)
    for x in X:
        if y_counter[x] > 0:
            num += x
            y_counter[x] -= 1
    num = ''.join(sorted(num, reverse=True))

    if not num:
        return '-1'
    elif num[0] == '0' and num[-1] == '0':
        return '0'
    return num
