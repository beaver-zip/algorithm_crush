# def solution(arr):
#     new = []
#     for i in range(1, len(arr)):
#         if arr[i-1] != arr[i]:
#             new.append(arr[i-1])
#     return new + [arr[-1]]

def solution(arr):
    new = []
    for i in arr:
        if new[-1:] == [i]: continue
        new.append(i)
    return new