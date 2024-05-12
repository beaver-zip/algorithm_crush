def solution(arr1, arr2):
    m, n = len(arr1), len(arr1[0])
    arr = [[0 for _ in range(n)] for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            arr[i][j] = arr1[i][j] + arr2[i][j]
    return arr

    # return [list(map(sum, zip(*x))) for x in zip(arr1, arr2)]
