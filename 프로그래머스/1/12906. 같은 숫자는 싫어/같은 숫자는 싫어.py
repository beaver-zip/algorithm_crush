def solution(arr):
    new = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            new.append(arr[i])
    return new