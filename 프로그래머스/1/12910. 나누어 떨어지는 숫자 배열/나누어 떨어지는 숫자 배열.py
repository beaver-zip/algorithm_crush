def solution(arr, divisor):
    ans = []
    for num in arr:
        if num % divisor == 0:
            ans.append(num)
    if not ans:
        ans.append(-1)
    return sorted(ans)