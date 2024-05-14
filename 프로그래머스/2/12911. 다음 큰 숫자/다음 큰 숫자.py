def solution(n):
    i = n
    n_b1 = bin(n).count('1')
    while i <= n or bin(i).count('1') != n_b1:
        i += 1
    return i