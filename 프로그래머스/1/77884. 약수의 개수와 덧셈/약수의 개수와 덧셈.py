def get_divisor(n):
    front = []
    back = []
    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            front.append(i)
            if i != n // i:
                back.append(n // i)
    return len(front + back[::-1])

def solution(left, right):
    result = 0
    for i in range(left, right+1):
        if get_divisor(i) % 2 == 0:
            result += i
        else:
            result -= i
    return result