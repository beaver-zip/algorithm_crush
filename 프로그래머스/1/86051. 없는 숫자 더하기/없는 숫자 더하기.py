def solution(numbers):
    summ = 0
    for i in '0123456789':
        if int(i) not in numbers:
            summ += int(i)
    return summ