def solution(name, yearning, photo):
    arr = []
    for pic in photo:
        score = 0
        for n, y in zip(name, yearning):
            if n in pic:
                score += y
        arr.append(score)
    return arr