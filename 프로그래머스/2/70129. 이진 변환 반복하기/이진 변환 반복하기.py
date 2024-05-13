def solution(s):
    cnt, zero = 0, 0
    while s != '1':
        cnt += 1
        num = s.count('1')
        zero += len(s) - num
        s = bin(num)[2:]
    return [cnt, zero]