def solution(n):
    text = ''
    for i in range(n): text += '수' if i % 2 == 0 else '박'
    return text